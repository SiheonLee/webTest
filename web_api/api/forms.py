from django.forms import ModelForm
from .models import Property


class PropertyExternalIdForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'