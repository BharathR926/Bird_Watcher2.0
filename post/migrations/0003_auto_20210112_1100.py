# Generated by Django 3.1.4 on 2021-01-12 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210112_1051'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='follow',
            table='Follow',
        ),
        migrations.AlterModelTable(
            name='post',
            table='Post',
        ),
        migrations.AlterModelTable(
            name='stream',
            table='stream',
        ),
    ]
