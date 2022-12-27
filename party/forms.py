from django.forms import ModelForm

from .models import Party


class PartyForm(ModelForm):

    class Meta:
        model = Party
        fields = [
        'title', 'date', 'time', 'restaurant', 'address', 'url',
        'subscriber', 'fee','comment','create_dt','mod_dt',
        ]
