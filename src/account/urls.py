from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from .view import register_user, index, credentials


urlpatterns = [
    url(r'^login', login, {'template_name':'login.html'}),
    url(r'^credentials', credentials, name='credentials'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^register', register_user, name='register'),
    url(r'^logout', logout, {'next_page': '/'}),
    url(r'^', index),
]