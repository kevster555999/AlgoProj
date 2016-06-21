from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^analytics/$', views.analytics, name='analytics'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^projects/$', views.projects, name='projects'),

    url(r'(?P<username>[a-zA-Z]+)/$', views.user, name='user'),
]
