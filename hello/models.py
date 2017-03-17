from django.db import models


# Create your models here.
class Person(models.Model):
    money = models.IntegerField(default=1000)
    name = models.CharField('姓名1', max_length=20)
    sex = models.CharField('性别', max_length=20)
