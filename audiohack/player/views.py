from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def player(request):
    '''
    Default Player page.
    '''
    ctx = RequestContext(request, {})
    
    return render_to_response('player.html', ctx )
