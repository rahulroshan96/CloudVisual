# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from forms import CredentialForm
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

def index(request):
    return redirect('/account/login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)

def credentials(request):
    msg = ''
    if request.method == 'GET':
        form = CredentialForm()
        args = {'form':form}
        return render(request, 'credentials.html', args)
    else:
        form = CredentialForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=request.user.username)
            form.user = user[0]
            form.save()
            msg = 'Credentials has been saved'
        return render(request, 'credentials.html', {'msg':msg, 'form':form})



