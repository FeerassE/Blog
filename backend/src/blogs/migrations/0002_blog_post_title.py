# Generated by Django 2.2.2 on 2019-06-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='title',
            field=models.CharField(default='title', max_length=150),
        ),
    ]