# Generated by Django 4.2.7 on 2023-11-11 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_date_addes_blogpost_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'blogposts'},
        ),
    ]
