from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.sample, name="api-sample" ),
    url(r'^save/$', views.save, name="api-save" ),
    url(r'^choices/$', views.choices, name="api-choices" ),
)