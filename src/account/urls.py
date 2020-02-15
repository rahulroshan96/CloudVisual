from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView
from .view import register_user, index, credentials



urlpatterns = [
    url(r'^login', LoginView.as_view(template_name='login.html')),
    url(r'^credentials', credentials, name='credentials'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^register', register_user, name='register'),
    url(r'^logout', LogoutView.as_view(next_page='/')),
    url(r'^', index),
]