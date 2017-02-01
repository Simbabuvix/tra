from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from itv.models import *

class AutenticacionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password': forms.PasswordInput(),}

class conductorForm(forms.ModelForm):
	class Meta:
		model = conductor
		fields= ['nombre','vehiculos']

class VehiculoForm(forms.ModelForm):
	class Meta:
		model = vehiculo
		fields= ['nombre','centro']

class ConForm(forms.ModelForm):
	class Meta:
		model = conductor
		fields= ['vehiculos']
