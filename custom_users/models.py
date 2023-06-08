from django.db import models
from django.contrib.auth.models import User


GENDER = (
    ('M', 'M'),
    ('Ж', 'Ж'),
)


class CustomUsers(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone_number = models.CharField(max_length=13, default='+996')
    age = models.PositiveIntegerField(default=16)
    gender = models.CharField(max_length=3, choices=GENDER)
    work = models.TextField(blank=True)


    def __str__(self):
        return self.username
