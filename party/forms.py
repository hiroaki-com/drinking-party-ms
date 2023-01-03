from django.forms import ModelForm
from django import forms
from django.forms import HiddenInput

from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

from .models import Party


class PartyCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(PartyCreateForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Party
        fields = [
        'user', 'title', 'date', 'time', 'restaurant', 'address', 'url',
        'subscriber', 'fee','comment',
        ]
        widgets = {
            'date': DatePickerInput(),
            'time': TimePickerInput(),
            'user': HiddenInput(),
        }
