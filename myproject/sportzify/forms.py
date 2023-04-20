from django.forms import ModelForm
from .models import *
from django import forms

class Formcreate(ModelForm):
    class Meta:
        model=customer
        fields = ['username','email','phone','password','password2','otp','aadhar']
        widgets = {
            'password': forms.PasswordInput(), 
            'password2': forms.PasswordInput()
        }
        

class TurfForm(ModelForm):
    class Meta:
        model=Turf
        fields=['turf_name','turf_address','turf_phone','turf_email','cost_per_hr','description','turf_image','ground_type']
        enctype='multipart/form-data'
        
        
