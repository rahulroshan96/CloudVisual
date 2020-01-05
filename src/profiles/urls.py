from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^resource/(?P<res_name>\w+)/(?P<res_type>\w+)', views.resource, name='resource'),
    url(r'^test$', views.az_graph, name='test'),
    url(r'^user$', views.user, name='user'),
    url(r'^azure$', views.az_graph, name='az_graph'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^', views.index, name='index'),
]