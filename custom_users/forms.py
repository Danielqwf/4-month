from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'M'),
    ('Ж', 'Ж'),
)

MARRIED = (
    ('Да', 'Да'),
    ('Нет', 'Нет'),
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    country = forms.CharField(max_length=100, required=True)
    region = forms.CharField(max_length=100, required=True)
    area = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=50, required=True)
    street = forms.CharField(max_length=40, required=True)
    house = forms.CharField(max_length=30, required=True)
    phone_number = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    married = forms.ChoiceField(choices=MARRIED, required=True)


    class Meta:
        model = models.CustomUsers
        fields = (
            'username', 'email', 'password1', 'password2', 'first_name',
            'last_name', 'country', 'region', 'area', 'city', 'street', 'house', 'phone_number',
            'age', 'gender', 'married'
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


