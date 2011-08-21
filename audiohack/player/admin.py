from django.contrib import admin
from models import Track, Annotation

class TrackAdmin(admin.ModelAdmin):
	pass


class AnnotationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Track, TrackAdmin)
admin.site.register(Annotation, AnnotationAdmin)
