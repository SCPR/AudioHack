from django.utils import simplejson
from django.http import HttpResponseServerError
from audiohack.player.models import Track, Annotation
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

        HttpResponse("Got json data")


'''
# JSON Sample

{
    "data": {
        "track": [
            {
                "length": 1000,
                "recorded_date": "1/1/2000",
                "soundcloud_id": "21597662",
                "title": "title for stuff",
                "url": "/path/to/stuff",
                "annotations": [
                    {
                        "description": "not much to add",
                        "end": 200,
                        "start": 100,
                        "type": "TE",
                        "url": "/url/to/the/goods"
                    }
                ]
            }
        ]
    },
    "user": "bob"
}'''