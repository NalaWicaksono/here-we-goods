from django.forms import ModelForm
from .models import Item  
from django import forms
from .models import Product

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["user"] 