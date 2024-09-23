from django import forms
from .models import SellerProduct

class SellerProductForm(forms.ModelForm):
    class Meta:
        model = SellerProduct
        fields = ('product_name', 'description', 'price', 'image')