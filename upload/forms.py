from django import forms
from .models import Uploader
from home.models import Product

class UploadForm(forms.ModelForm):
    #  myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    class Meta:
        model = Product;
        
        labels = {
            'uploaded_by': ('Your Id'),
        }
        widgets = {
            
            'name' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Enter Name of the Product",
            }),
            
            'uploaded_by' : forms.TextInput(attrs = {
                'class': "form-control",
                "readonly" : True,
            }),
            
            
            'quantity' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Quantity of the product",
            }),
            
            
            
        }
        
        fields = [
            "name",
            "category",
            "image",
            "price",
            "quantity",
            "uploaded_by",
           
         ]
        

class UploaderLoginForm(forms.ModelForm):
    class Meta:
        model = Uploader;
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
        
        
        
        
        
class UploaderRegisterForm(forms.ModelForm):
    class Meta:
        model = Uploader;
        widgets = {
            'mob_no' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Mobile Number",
                'readonly' : True,
            }),
            
            'full_name' : forms.TextInput(attrs = {
                'class': "form-control",
                'placeholder': "Enter Your Full Name",
                'length': 10,
            }),
            
            
        }
        
        fields = [
            "full_name",
            "mob_no",
            
        ]
        
     