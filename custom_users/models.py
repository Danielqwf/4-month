from django.db import models
from django.contrib.auth.models import User


GENDER = (
    ('M', 'M'),
    ('Ж', 'Ж'),
)

MARRIED = (
    ('Да', 'Да'),
    ('Нет', 'Нет'),
)

class CustomUsers(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    country = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=40, null=True)
    house = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=13, default='+996')
    age = models.PositiveIntegerField(default=16)
    gender = models.CharField(max_length=3, choices=GENDER)
    about = models.TextField(max_length=100, blank=True, null=True)
    married = models.CharField(max_length=3, blank=True, null=True, choices=MARRIED)




    def __str__(self):
        return self.username
