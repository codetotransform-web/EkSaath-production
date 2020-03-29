from django import forms
from .models import Customer


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer;
        widgets = {
            'full_name' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Full Name",
            }),
            
            'mob_no' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Full Name",
                'length': 10,
                'readonly' : True,
            }),
            'city': forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "City",
                
            }),
            'colony' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Enter Colony Name",
            }),
            
            
        }
        
        fields = [
            "full_name",
            "mob_no",
            "city",
            "colony",
            # "location"
        ]
        
        
        
        
class CustomerLoginForm(forms.ModelForm):
    class Meta:
        model = Customer;
        widgets = {
            
            'mob_no' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Enter Your 10 digit Mobile Number",
                'length': 10,
            }),
            
            
            
        }
        
        fields = [
            "mob_no",
           
        ]