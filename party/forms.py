from django.forms import ModelForm

from .models import Party


class PartyForm(ModelForm):

    class Meta:
        model = Party
        fields = [
        'user', 'title', 'date', 'time', 'restaurant', 'address', 'url',
        'subscriber', 'fee','comment','create_dt','mod_dt',
        ]

# TODO: NULL制約により、user,create_dt,mod_dt の登録が必須となっているため、対処する