# Generated by Django 4.0.5 on 2022-08-10 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_alter_productrating_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='created_at',
        ),
    ]
