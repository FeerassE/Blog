# Generated by Django 2.2.2 on 2019-06-11 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20190611_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_post',
            old_name='user',
            new_name='userid',
        ),
    ]
