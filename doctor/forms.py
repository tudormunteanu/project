from django import forms
from django.forms import ModelForm
from .models import Doctor

#create form from defined model

class DoctorForm(ModelForm):

    class Meta:
    	model = Doctor
    	fields = ['first_name', 'last_name', 'email']

    def __str__(self): #not mandatory

    	return self.name 
