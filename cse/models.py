from django.db import models
from django.contrib.auth.models import User



class display(models.Model):
    data = models.TextField(null=True , blank = True )

class details(models.Model):
    name = models.CharField(max_length = 200 ,null=True , blank = True)
    email = models.EmailField(null=True , blank = True)
    description = models.TextField(null=True , blank = True)

    def __str__(self):
        return self.name

class cp(models.Model):
    title = models.TextField(null=True , blank = True)
    data = models.TextField(null=True , blank = True)
    question = models.TextField(null=True , blank = True)


    def __str__(self):
        return self.title

    
# Create your models here.
