from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class TrackForm(ModelForm):
    class Meta:
        model = Track

class AnnotationForm(ModelForm):
    class Meta:
        model = Annotation
