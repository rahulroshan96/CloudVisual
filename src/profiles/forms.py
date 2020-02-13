from django import forms
from models import UserInputModel


class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInputModel
        fields = ['user_input']