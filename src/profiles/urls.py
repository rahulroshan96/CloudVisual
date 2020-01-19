from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^resource/(?P<res_name>\w+)/(?P<res_type>\w+)', view.resource, name='resource'),
    url(r'^test$', view.az_graph, name='test'),
    url(r'^user$', view.user, name='user'),
    url(r'^azure$', view.az_graph, name='az_graph'),
    url(r'^youtube$', view.youtube, name='youtube'),
    url(r'^example$', view.example, name='example'),
    url(r'^dashboard$', view.dashboard, name='dashboard'),
    url(r'^', view.index, name='index'),
]