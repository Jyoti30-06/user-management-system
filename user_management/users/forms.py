from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email', 'name', 'texture', 'whatsapp', 'volume', 'dob', 'scalp',
            'place_of_birth', 'combinghair', 'year', 'cut', 'heat', 'colour',
            'hairtangle', 'oil', 'hairfall', 'shampoo', 'oilweek', 'conditioner',
            'haircomb', 'hairwash', 'chemicaltreatment', 'hairdry', 'treatment'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'texture': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.NumberInput(attrs={'class': 'form-control'}),
            'volume': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'scalp': forms.TextInput(attrs={'class': 'form-control'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'combinghair': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'cut': forms.TextInput(attrs={'class': 'form-control'}),
            'heat': forms.TextInput(attrs={'class': 'form-control'}),
            'colour': forms.TextInput(attrs={'class': 'form-control'}),
            'hairtangle': forms.TextInput(attrs={'class': 'form-control'}),
            'oil': forms.TextInput(attrs={'class': 'form-control'}),
            'hairfall': forms.TextInput(attrs={'class': 'form-control'}),
            'shampoo': forms.TextInput(attrs={'class': 'form-control'}),
            'oilweek': forms.TextInput(attrs={'class': 'form-control'}),
            'conditioner': forms.TextInput(attrs={'class': 'form-control'}),
            'haircomb': forms.TextInput(attrs={'class': 'form-control'}),
            'hairwash': forms.TextInput(attrs={'class': 'form-control'}),
            'chemicaltreatment': forms.TextInput(attrs={'class': 'form-control'}),
            'hairdry': forms.TextInput(attrs={'class': 'form-control'}),
            'treatment': forms.TextInput(attrs={'class': 'form-control'}),
        }
