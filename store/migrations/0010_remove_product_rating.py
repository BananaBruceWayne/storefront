# Generated by Django 4.0.5 on 2022-07-25 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_productrating_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]