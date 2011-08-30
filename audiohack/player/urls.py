from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'^tracks/(?P<track>\d+)$', views.track,),
    url(r'^tracks/(?P<track>\d+)/annotate/', views.annotate,),
    url(r'^$', views.player, name="player-player" ),
)
