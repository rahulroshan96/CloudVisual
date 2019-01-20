from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resource/(?P<res_name>\w+)/(?P<res_type>\w+)', views.resource, name='resource'),
    url(r'^test', views.test, name='test'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^', views.index, name='index'),
]