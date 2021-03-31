
from django import forms
from .models import Product,merchant


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    date_added= forms.DateTimeField(auto_now_add=True)



class merchantform(forms.Form):
    user = forms.ModelChoiceField(queryset=Users.objects.all())