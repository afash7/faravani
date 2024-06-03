from django import forms

class VerificationForm(forms.Form):
    phone_number = forms.CharField(max_length=15, required=True)
    verification_code = forms.CharField(max_length=6, required=True)
