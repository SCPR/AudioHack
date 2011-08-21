import views

urlpatterns = patterns('',
    url(r'^$', views.save, name="api-save" ),
)