# Generated by Django 3.1 on 2021-05-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0003_auto_20210522_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
