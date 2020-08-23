from django import forms
from django.forms import ModelForm

from .models import *


class DataForm(ModelForm):

    class Meta:

        model = userForm
        fields = '__all__'
