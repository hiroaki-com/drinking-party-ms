from django.forms import ModelForm
from django import forms

from .models import Party


class PartyCreateForm(ModelForm):

    class Meta:
        model = Party
        fields = [
        'user', 'title', 'date', 'time', 'restaurant', 'address', 'url',
        'subscriber', 'fee','comment','create_dt','mod_dt',
        ]
        widgets = {
            'date': forms.SelectDateWidget,
        }

# TODO: NULL制約により、user,create_dt,mod_dt の登録が必須となっているため、対処する