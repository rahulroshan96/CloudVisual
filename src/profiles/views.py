# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
import random
import jsonpickle
import time
from django.contrib.auth.models import User
from account.models import Credentials


def get_token(request):
    user = User.objects.get(username=request.user)
    creds = Credentials.objects.filter(user=user)[0]
    curr_time = int(time.time())
    if int(creds.token_expire_on) > curr_time:
        print 'Fetching token from DB'
        return creds.bearer_token, str(creds.subscription_id)
    auth = {
        'tenant_id': str(creds.tenant_id),
        'client_secret': str(creds.secret_key),
        'client_id': str(creds.client_id),
        'resource': 'https://management.azure.com/',
        'grant_type': 'client_credentials'
    }
    url = 'https://login.microsoftonline.com/%s/oauth2/token'%str(creds.tenant_id)
    result = requests.post(url, data=auth)
    result = json.loads(result.text)
    token = "Bearer %s" % result['access_token']
    creds.bearer_token = token
    creds.token_expire_on = result['expires_on']
    creds.save(update_fields=['bearer_token', 'token_expire_on'])
    return token, str(creds.subscription_id)

def resource(self, res_name, res_type):
    return HttpResponse("<h1> Name is: "+res_name + ' and type is: '+ res_type+"</h1>")


def get_vm_details(vm, token, group=0 ):
    data = {}
    data['nodes'] = []
    data['links'] = []
    vm_name = vm['name']
    nic_name = vm['properties']['networkProfile']['networkInterfaces'][0]['id'].split('/')[-1]
    disk_name = vm['properties']['storageProfile']['osDisk']['name']
    try:
        boot_diagnostic = vm['properties']['diagnosticsProfile']['bootDiagnostics']['storageUri'].split('.')[0].split('//')[1]
    except:
        boot_diagnostic = None
    location = vm['location']
    attributes = [(vm_name, 'vm'), (nic_name, 'nic'), (disk_name, 'disk'), (boot_diagnostic, 'bootd')]
    for attr in attributes:
        if attr[0]:
            temp = {}
            temp['id'] = attr[0]
            temp['group'] = group
            temp['type'] = attr[1]
            data['nodes'].append(temp)
            if attr != vm['name']:
                temp = {}
                temp['source'] = attr[0]
                temp['target'] = vm['name']
                temp['value'] = random.randint(1,21)
                data['links'].append(temp)
    vm_data = {}
    vm_data['result'] = data
    return vm_data

def az_graph(request):

    token, subscription_id = get_token(request)
    url_vm = 'https://management.azure.com/subscriptions/%s/resourceGroups/rahulr-resource-group/providers/Microsoft.Compute/virtualMachines?api-version=2018-06-01'%subscription_id
    res = requests.get(url_vm, headers={'Authorization': token})
    all_vm_data = vm = json.loads(res.text)
    data = {}
    data['result'] = {}
    data['result']['nodes'] = []
    data['result']['links'] = []
    for i, d in enumerate(all_vm_data['value']):
        temp = get_vm_details(d,token, i+1)
        data['result']['nodes'].extend(temp['result']['nodes'])
        data['result']['links'].extend(temp['result']['links'])
    data['result'] = jsonpickle.encode(data['result'])
    return render(request, 'azure_graph.html', context=data)

def index(request):
    return redirect('/account/login')

def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    else:
        return redirect('/account/login')

def user(request):
    return render(request, 'user.html')





