from django import forms
from django.forms import ModelForm
from .models import Doctor

#create form from defined model

class DoctorForm(ModelForm):
    name = models.CharField(label='Your name', max_length=100)

    def __str__(self):

    	return self.name
