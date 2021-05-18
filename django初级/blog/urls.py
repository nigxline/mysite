from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^article/$', views.article, name='article'),
    url(r'^about/$', views.about, name='about'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^resource/$', views.resource, name='resource'),
    # url(r'^detail/(?<pk>[0-9]+)/$', views.detail, name='detail'),
]