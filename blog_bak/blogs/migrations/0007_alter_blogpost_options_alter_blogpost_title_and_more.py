# Generated by Django 4.2.7 on 2023-11-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]