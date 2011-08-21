import urllib2
import simplejson
from lxml import html
from email.MIMEText import MIMEText
import smtplib

GMAIL_LOGIN = 'pyladiestest@gmail.com'
GMAIL_PASSWORD = 't3st1ng!'

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
    tds = get_all_tags(url,'td.listItem')
    items = [l for l in tds if 'headers' in l.attrib.keys() and l.attrib['headers'] == 'Audio Link']
    links = []
    for i in items:
        for l in i.iterdescendants():
            if 'onclick' in l.attrib.keys():
                links.append(l.attrib['onclick'].split(',')[0].replace('window.open(','').lstrip("'").rstrip("'"))
    
    return links

def scrape_city_hall(url):
    items = get_all_tags(url, 'div#all_Items div.items') 






