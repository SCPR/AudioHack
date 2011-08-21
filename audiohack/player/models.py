from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ("url", "title")

class AnnotationForm(ModelForm):
    class Meta:
        model = Annotation
        fields = ("start", "end", "type", "url", "description")
