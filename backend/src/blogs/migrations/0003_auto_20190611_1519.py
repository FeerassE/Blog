# Generated by Django 2.2.2 on 2019-06-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='content',
            field=models.TextField(),
        ),
    ]
