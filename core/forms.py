from django import forms

class BasicForm(forms.Form):
    company_email_address = forms.EmailField()
    phone_number = forms.CharField(label='Phone')
    company_size = forms.CharField()
    office_adress = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    
    