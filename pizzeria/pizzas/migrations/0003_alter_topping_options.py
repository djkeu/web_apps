# Generated by Django 4.2.7 on 2023-11-06 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'entries'},
        ),
    ]