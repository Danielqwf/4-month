from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'M'),
    ('Ж', 'Ж'),
)

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(required=True, choices=GENDER)
    work = forms.CharField(max_length=100)


    class Meta:
        model = models.CustomUsers
        fields = (
            'username', 'email', 'password1', 'password2', 'first_name',
            'last_name', 'age', 'gender', 'phone_number', 'work'
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


