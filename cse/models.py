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

class dev(models.Model):
    topic = models.TextField(null=True , blank =True)
    session  = models.URLField(max_length = 300 , null=True , blank =True)
    resource = models.TextField(null=True , blank =True)

    def __str__(self):
        return self.topic


class problemofday(models.Model):
    problem_of_the_day = models.URLField(max_length = 300 , null=True , blank =True)
    old_questions = models.TextField(null=True , blank =True)
    # rating = models.CharField()
    # tag models.CharField()

    
# Create your models here.
