from django.db import models

# Create your models here.
class MyModel(models.Model):
    a = models.IntegerField()
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=100)
    d = models.FloatField()
    

class MyTable(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 , unique=True)


class Member(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name