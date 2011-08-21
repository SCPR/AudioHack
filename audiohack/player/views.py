from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from audiohack.player.models import Track, Annotation

def player(request):
    '''
    Default Player page.
    '''
    ctx = RequestContext(request, {})
    
    return render_to_response('player.html', ctx )

def all_tracks(request):
    '''
    Display all tracks
    ''''
    pass

def track(request):
    '''
    Single track page
    '''
    pass
    
def annotate(request, track):
    '''
    Add annotation
    '''
    pass

def add_track(request):
    '''
    Add a track to the audio cloud
    '''
    
