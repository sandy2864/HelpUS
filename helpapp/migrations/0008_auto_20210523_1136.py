# Generated by Django 3.1 on 2021-05-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0007_image_mob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='mob',
            new_name='Desc',
        ),
    ]
