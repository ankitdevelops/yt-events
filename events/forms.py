from django import forms
from django import forms
from . models import Event
from django.contrib.admin.widgets import AdminDateWidget

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "scheduled_on":forms.DateInput(
                attrs= {
                    "class": "form-control ",
                     "type":'datetime-local'
                }
            )
        }