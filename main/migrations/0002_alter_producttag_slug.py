# Generated by Django 3.2.4 on 2021-06-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttag',
            name='slug',
            field=models.SlugField(max_length=48, unique=True),
        ),
    ]
