from django.db import models


class user(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
