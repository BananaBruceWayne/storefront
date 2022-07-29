# Generated by Django 4.0.5 on 2022-07-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_productrating_user_productrating_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productrating',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='productrating',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='productrating',
            name='User',
        ),
        migrations.AddField(
            model_name='productrating',
            name='user',
            field=models.ManyToManyField(blank=True, to='store.customer'),
        ),
    ]
