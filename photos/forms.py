from .models import Photo
from django import forms
from django.forms import ModelForm

class photo_form(ModelForm):
    forms.DateInput.input_type = "date"
    # photo = forms.ImageField()
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ('reviewed','likes')
