from django.forms import ModelForm
from locator.models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('name',)