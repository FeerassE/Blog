from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)

class Blog_Post(models.Model):
    pub_date = models.DateField(default=datetime.date.today)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=150, default="title")