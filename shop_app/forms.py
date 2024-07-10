from django import forms
from django.core import validators
from django.contrib.auth.models import Group
from shop_app.models import Product,ProductImage




class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


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
        fields="name","price","description","discount","preview"

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields="name",


class ProductFormN(forms.ModelForm):
    class Meta:
        model=Product
        fields="name","description","price","discount","preview"
    images=MultipleFileField()