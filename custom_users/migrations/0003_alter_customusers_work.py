# Generated by Django 4.2.1 on 2023-06-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_customusers_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='work',
            field=models.TextField(blank=True, null=True),
        ),
    ]
