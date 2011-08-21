from django.utils import simplejson
from django.http import HttpResponseServerError, HttpResponse
from audiohack.player.models import Track, Annotation, ANNOTATION_CHOICES
from django.contrib.auth.models import User

def save(request):
    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
        try:
            data = json_data['data']
            user = request.user
        except KeyError:
            HttpResponseServerError("Malformed data!")

        if 'track' in json_data['data']:
            '''Add tracks'''
            
            for track in json_data['data']['track']:
                if "url" in track:
                    t = Track(url=track['url'], user=user)
                        
                    if track['length']:
                        t.length = track['length']

                    if track['recorded_date']:
                        t.recorded_date = track['recorded_date']

                    if track['soundcloud_id']:
                        t.soundcloud_id = track['soundcloud_id']
                    
                    t.save()
                    
                    if "annotations" in track:
                        for ann in track['annotations']:
                            if "url" in ann:
                                a = Annotation(url=ann['url'], track=t, user=user)
                    
                                if track['start']:
                                    t.start = track['start']

                                if track['end']:
                                    t.end = track['end']

                                if track['type']:
                                    t.type = track['type']

                                if track['description']:
                                    t.description = track['description']

                                a.save()

        return HttpResponse("Got json data")

    return HttpResponse("JSON only, please.", mimetype="text/plain")


def choices(request):
    return HttpResponse(simplejson.dumps( {'annotation_choices':ANNOTATION_CHOICES}, sort_keys=True, indent=4 ), mimetype="text/json")


def sample(request):
    sample = {'data': {'track': [{'annotations': [{'description': 'not much to add',
                                          'end': 200,
                                          'start': 100,
                                          'type': 'TE',
                                          'url': '/url/to/the/goods'}],
                         'length': 1000,
                         'recorded_date': '1/1/2000',
                         'soundcloud_id': '21597662',
                         'title': 'title for stuff',
                         'url': '/path/to/stuff'}]},
              'user': 'bob'}

    return HttpResponse(simplejson.dumps( sample, sort_keys=True, indent=4 ), mimetype="text/json")
