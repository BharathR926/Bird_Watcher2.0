# Generated by Django 3.1.4 on 2021-01-12 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210112_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Url',
            new_name='caption',
        ),
    ]
