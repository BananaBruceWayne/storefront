# Generated by Django 4.0.5 on 2022-07-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_rename_product_productrating_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='user',
        ),
    ]