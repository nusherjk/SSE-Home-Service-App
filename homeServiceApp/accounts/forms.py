# forms.py
from django import forms
from .models import Customer
from django_countries.fields import CountryField

class CustomerRegisterForm(forms.ModelForm):

    retype_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype your password'}),
        label='Retype Password',
        min_length=8
    )
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'dob', 'email', 'country', 'C19Vaccinated', 'profession', 'password']
        labels = {
            'first_name': 'First Name',
            'Last_name': 'Last Name',
            'dob': 'Date of Birth',
            'email': 'Email Address',
            'country': 'Country of Citizenship',
            'C19Vaccinated': 'COVID-19 Vaccinated',
            'profession': 'Profession',
            'password': 'Password'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': 'required'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': 'required'}),
            'country': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'C19Vaccinated': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profession': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Profession', 'required': 'required'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}),
        }
