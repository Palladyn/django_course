from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserDataForm(forms.Form):
    name=forms.CharField(label="Имя пользователя",max_length=100)
    age=forms.IntegerField(label="Возраст",min_value=1,max_value=120)
    user_info=forms.CharField(label="Информация о пользователе",widget=forms.Textarea)


def Valid_file_name(file:InMemoryUploadedFile ):
    if file.name and "virus" in file.name:
        raise ValidationError("Обнаружен ВИРУС")

class Upload_file(forms.Form):
    file=forms.FileField(validators=[Valid_file_name])