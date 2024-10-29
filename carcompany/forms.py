from django import forms 
from .models import *

class ComapanyForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = ("name_company","country","create_at","image")

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ("car_model","speed","color","company_id","probeg","price","image")
