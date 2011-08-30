from datetime import datetime
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Track(models.Model):
    '''
    Track model contains the base audio file paths 
    '''
    user = models.ForeignKey(User)
    url = models.URLField(blank=True,null=True)         # Path to the Track (usually a sound cloud file)
    title = models.CharField(max_length='200')          # 
    length = models.IntegerField()                      # in milliseconds
    recorded_date = models.DateField()                  #
    soundcloud_id = models.CharField(max_length='15',blank=True,null=True)               #
    added_timestamp = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User)             #

ANNOTATION_CHOICES = (
    (u'TE', u'TEXT'),
    (u'IM', u'IMAGE'),
    (u'TW', u'TWITTER'),
    (u'WB', u'WEBPAGE'),
    (u'MP', u'LOCATION'),
    )

class Annotation(models.Model):
    '''
    Annotations are files and extra information attached to Tracks
    '''
    user = models.ForeignKey(User)
    start = models.IntegerField()
    end = models.IntegerField()
    type = models.CharField(max_length=2, choices = ANNOTATION_CHOICES)
    url = models.URLField(blank=True,null=True)
    description = models.TextField()
    track = models.ForeignKey('Track')
    added_timestamp = models.DateTimeField(default=datetime.now)
           #

    def serialize_annotation(self):
        
        #choice = None
        
        #for ann in ANNOTATION_CHOICES:
        #    if ann[0] == self.type:
        #        choice = ann[1]
                
        result = {'start':self.start, 'end':self.end, 'type':self.get_type_display() }
        
        if self.url:
            result['url'] = self.url
        
        if self.description:
            result['description'] = self.description
        
        return result
        

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ("url", "title")

class AnnotationForm(ModelForm):
    class Meta:
        model = Annotation
        fields = ("start", "end", "type", "url", "description")
