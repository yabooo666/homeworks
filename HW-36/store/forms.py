from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "description",
            "price",
            "has_discount",
            "discount_price",
            "is_available",
            "image",
        ]
        widgets = {
            "category": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "მაგ: MacBook Pro 16 M3"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "პროდუქტის დეტალური აღწერა..."}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "0.00"}),
            "has_discount": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
            "discount_price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "0.00"}),
            "is_available": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
