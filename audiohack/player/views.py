from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from player.models import Track, Annotation, TrackForm, AnnotationForm

def player(request):
    '''
    Default Player page.
    '''
    ctx = RequestContext(request, {})
    user = User.objects.get(pk=1)       # For testing purposes
    
    return render_to_response('player/player.html', ctx )

def all_tracks(request):
    '''
    Display last 10 tracks added
    '''
    tracks = Track.objects.order_by('-added_timestamp')[:9]
    ctx = RequestContext(request, {'tracks':tracks})
    return render_to_response('player/tracks.html', ctx)

def track(request, track):
    ''' 
    Single track page
    '''
    track = Track.objects.get(id=track)
    annotations = Annotation.objects.filter(track=track)
    ctx = RequestContext(request, {'track':track, 'annotations':annotations})
    return render_to_response('player/track.html', ctx)
    
def annotate(request, track):
    '''
    Add annotation
    '''
    form = AnnotationForm()
    ctx = RequestContext(request, {'form':form})    
    return render_to_response('player/annotate.html', ctx )
    

def add_track(request):
    '''
    Add a track to the audio cloud
    '''
    
    pass
