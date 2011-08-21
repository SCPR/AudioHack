import urllib2
import simplejson
from lxml import html
from email.MIMEText import MIMEText
import smtplib
from datetime import datetime
import os,sys
sys.path.append(os.path.dirname(os.getcwd()))
import re
from audiohack import settings
from audiohack.player.models import User, Track, Annotation

os.environ['DJANGO_SETTINGS_MODULE'] = 'audiohack.settings'


GMAIL_LOGIN = 'pyladiestest@gmail.com'
GMAIL_PASSWORD = 't3st1ng!'



""" To run this go to python manage.py shell for your project.

    Then:
        
        import sys,os
        sys.path.append(os.path.dirname(os.getcwd()))
        from scraper.scraper import scraper_main
        scraper_main()
"""


def send_email(subject, message, from_addr=GMAIL_LOGIN, to_addr=GMAIL_LOGIN):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Reply-To'] = 'happyhours@noreply.com'
                    
    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(GMAIL_LOGIN,GMAIL_PASSWORD)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.close()


def get_site_html(url):
    source = urllib2.urlopen(url).read()
    return source


def get_all_tags(url,tag):
    source = get_site_html(url)
    tree = html.document_fromstring(source)
    return tree.cssselect(tag)


def get_all_city_hall_pages():
    url = 'http://lacity.granicus.com/ViewPublisher.php?view_id=103'
    trs = get_all_tags(url,'tr')
    items = []
    for t in trs:
        tds = t.findall('td')
        if len(tds) < 6: continue
        new_item = {}
        for l in tds:
            if 'headers' not in l.attrib: continue
            if 'Name' == l.attrib['headers']:
                new_item['title'] =  l.text_content()
            if 'Audio Link' == l.attrib['headers']:
                audio_link = [a for a in l.findall('a') if 'onclick' in a.attrib.keys()][0].attrib['onclick']
                new_item['link'] = audio_link.split(',')[0].replace('window.open(','').lstrip("'").rstrip("'")
            if 'Date' in l.attrib['headers']:
                new_item['date'] = datetime.strptime(l.text_content(),'%m/%d/%y')
            if 'Duration' in l.attrib['headers']:
                duration =  l.text_content()
                hours = re.search('\d+h',duration).group().rstrip('h')
                mins = re.search('\d+m',duration).group().rstrip('m')
                new_item['duration'] = (int(hours) * 60 * 60) + (int(mins) * 60) * 1000
        items.append(new_item)

    return items

def scrape_city_hall(url):
    content = get_all_tags(url, 'div#all_Items')
    if not len(content): return False
    ch_list = []
    for i in content[0].iterchildren():
        ch_dict = {}
        audio_link = i.find('a')
        if 'onclick' in audio_link.attrib:
            ch_dict['time'] = int(audio_link.attrib['onclick'].split("'")[1].lstrip('0:'))
        ch_dict['text'] = i.text_content()
        ch_list.append(ch_dict)
    return ch_list



def scraper_main():
    items = get_all_city_hall_pages()
    for i in items:
        notes = scrape_city_hall(i['link'])
        i['notes'] = notes
        if not notes:
            items.remove(i)
    try:
        user = User.objects.get(username='scraper_bot')
    except User.DoesNotExist:
        user = User.objects.create(username='scraper_bot')
        user.set_password('b0tal0t')
        user.save()
    for i in items:
        try:
            track = Track.objects.get(title=i['title'],recorded_date=i['date'],user=user,length=i['duration'])
            print 'Got track...',i['title']
        except Track.DoesNotExist:
            print 'Creating track...',i['title']
            track = Track.objects.create(title=i['title'],recorded_date=i['date'],user=user,length=i['duration'])
            track.save()

        if 'notes' not in i.keys(): continue
        
        for n in i['notes']:
            try:
                note = Annotation.objects.get(start=n['time'],end=n['time']+3,description=n['text'],type='TE',track=track,user=user)
                print 'Got note...',n['text']
            except Annotation.DoesNotExist:
                print 'Creating note...',n['text']
                note = Annotation.objects.create(start=n['time'],end=n['time']+3,description=n['text'],type='TE',track=track,user=user)
                note.save()

if __name__ == '__main__':
    scraper_main()

