# forms.py
from django import forms
from .models import Customer, Address
from django_countries.fields import CountryField



class UpdateProfileForm(forms.ModelForm):


    class Meta():
        model = Customer
        fields = ['first_name', 'last_name', 'dob',  'country', 'C19Vaccinated', 'profession']
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
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1',
                       'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1',
                       'placeholder': 'Last Name', 'required': 'required'}),
            'dob': forms.DateInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1',
                       'type': 'date', 'required': 'required'}),
            # 'email': forms.EmailInput(
            #     attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full',
            #            'placeholder': 'Email', 'required': 'required'}),
            'country': forms.Select(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1',
                       'required': 'required'}),
            'C19Vaccinated': forms.CheckboxInput(
                attrs={'class': 'border-gray focus-action-1', 'id': "form_1_checkbox"}),
            'profession': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1',
                       'placeholder': 'Profession', 'required': 'required'}),
            # 'password': forms.PasswordInput(
            #     attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full',
            #            'placeholder': 'Password', 'required': 'required'}),
        }




class AddressForm(forms.ModelForm):
    class Meta():
        model = Address
        fields = ['line1','line2', 'suburb','postcode', 'state']
        widgets = {
            'line1': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1 ', 'placeholder': 'Line 1', 'required': 'required'}),
            'line2': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1', 'placeholder': 'Line 2' }),
            'suburb': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1', 'placeholder': 'Suburb Name', 'required': 'required'}),
            'postcode': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1', 'placeholder': 'Post Code', 'required': 'required'}),
            'state': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading my-1', 'placeholder': 'State', 'required': 'required'})

        }
class CustomerRegisterForm(forms.ModelForm):

    retype_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'placeholder': 'Retype your password'}),
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
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'placeholder': 'Last Name', 'required': 'required'}),
            'dob': forms.DateInput(attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'type': 'date', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'placeholder': 'Email', 'required': 'required'}),
            'country': forms.Select(attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'required': 'required'}),
            'C19Vaccinated': forms.CheckboxInput(attrs={'class': 'border-gray focus-action-1', 'id': "form_1_checkbox" }),
            'profession': forms.TextInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'placeholder': 'Profession', 'required': 'required'}),
            'password': forms.PasswordInput(
                attrs={'class': 'input border-gray focus-action-1 color-heading placeholder-heading w-full', 'placeholder': 'Password', 'required': 'required'}),
        }



