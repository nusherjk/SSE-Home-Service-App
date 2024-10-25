from django import forms
from .models import Booking, Review, Service, ProviderProfile


class BookingForm(forms.ModelForm):
    # service = forms.ModelChoiceField(
    #     queryset=Service.objects.all(),  # Replace with your model's queryset
    #     required=True,  # Make it optional by setting required=False
    #     label="Select Services"
    # )
    #
    # provider = forms.ModelChoiceField(
    #     queryset= ProviderProfile.objects.filter(services=service), required=True, label="Select Provider"
    # )
    class Meta:


        model = Booking
        fields = ['service', 'provider', 'date', 'time', 'address', 'notes']

        widgets = {

            # 'provider': forms.TextInput(
            #     attrs={'class': 'form-control', 'placeholder': 'Provider Name', 'required': 'required'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            # 'time': forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'required': 'required'})),
            'address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Address', 'required': 'required'}),

            'notes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
