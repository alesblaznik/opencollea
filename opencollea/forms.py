from django import forms
from opencollea.models import *


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['date_joined', 'last_login']
