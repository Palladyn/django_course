from django import forms
from django.core import validators
from django.contrib.auth.models import Group
from shop_app.models import Product


# class ProductForms(forms.Form):
#     name=forms.CharField(max_length=100,label="Наименование товара")
#     price=forms.DecimalField(min_value=1,max_value=1000000, label="Цена товара",decimal_places=2)
#     description=forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":30}),
#                                 label="Описание товара",
#                                 validators=[validators.RegexValidator
#                                             (regex=f"great",
#                                              message="Описание должно содержать слово great")
#                                             ],)

class ProductForms(forms.ModelForm):
    class Meta:
        model=Product
        fields="name","price","description","discount"

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields="name",