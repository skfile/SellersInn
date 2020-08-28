from django import forms
from django.forms import ModelForm

from .models import *


class DataForm(ModelForm):

    class Meta:

        model = userForm
        fields = '__all__'


class EmailForm(ModelForm):

    class Meta:

        model = newsletter
        fields = '__all__'
