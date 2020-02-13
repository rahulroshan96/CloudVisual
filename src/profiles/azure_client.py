import requests
from django.contrib.auth.models import User
import json
from account.models import Credentials
import time


class Azure_Client(object):
    def __init__(self, username):
        print 'Initializing Azure Client'
        self.subscription_id = None
        self.token = self.get_token(username)

    def get_token(self, username):
        user = User.objects.get(username=username)
        creds = Credentials.objects.filter(user=user)[0]
        curr_time = int(time.time())
        self.subscription_id = str(creds.subscription_id)

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
        url = 'https://login.microsoftonline.com/%s/oauth2/token' % str(creds.tenant_id)
        result = requests.post(url, data=auth)
        result = json.loads(result.text)
        token = "Bearer %s" % result['access_token']
        creds.bearer_token = token
        creds.token_expire_on = result['expires_on']
        creds.save(update_fields=['bearer_token', 'token_expire_on'])
        return token

    def get_all_vm(self, rg):
        url_vm = 'https://management.azure.com/subscriptions/%s/resourceGroups/rahulr-resource-group/providers/Microsoft.Compute/virtualMachines?api-version=2018-06-01' % self.subscription_id
        res = requests.get(url_vm, headers={'Authorization': self.token})


if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    obj = Azure_Client('aviuser')
    print 'hello'