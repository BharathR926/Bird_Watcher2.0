# Generated by Django 3.1.4 on 2020-12-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_likes'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]
