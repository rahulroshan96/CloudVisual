from .models import Credentials
from django.forms.models import ModelForm


class CredentialForm(ModelForm):
    class Meta:
        model = Credentials
        fields = ['credential_name', 'client_id', 'secret_key', 'tenant_id', 'subscription_id']


