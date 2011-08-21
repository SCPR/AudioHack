from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Track(models.Model):
    '''
    Track model contains the base audio file paths 
    '''
    url = models.URLField()                             # Path to the Track (usually a sound cloud file)
    title = models.CharField(max_length='200')          # 
    length = models.IntegerField()                      # in milliseconds
    recorded_date = models.DateField()                  #
    soundcloud_id = models.CharField(max_length='15')               #

ANNOTATION_CHOICES = (
    (u'TE', u'Text'),
    (u'IM', u'Image'),
    (u'TW', u'Twitter'),
    (u'WB', u'Web Page'),
    (u'MP', u'Map/Location'),
    )

class Annotation(models.Model):
    '''
    Annotations are files and extra information attached to Tracks
    '''
    user = models.ForeignKey(User)
    start = models.IntegerField()
    end = models.IntegerField()
    type = models.CharField(max_length=2, choices = ANNOTATION_CHOICES)
    url = models.URLField()
    description = models.TextField()
    track = models.ForeignKey('Track')
           #

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ("url", "title")

class AnnotationForm(ModelForm):
    class Meta:
        model = Annotation
        fields = ("start", "end", "type", "url", "description")
