from django.db import models
from django.contrib.auth.models import User




class semester(models.Model):
    sem = models.CharField(max_length = 200 , null=True , blank = True)
    subjects = models.TextField(null= True , blank=True)

    def __str__(self):
        return self.sem


class subject(models.Model):
    name = models.CharField(max_length = 200 , null=True , blank = True)
    book = models.TextField(null=True , blank =True)
    other = models.TextField(null=True , blank =True)

    def __str__(self):
        return self.name


class books(models.Model):
    sub = models.ForeignKey(subject, on_delete=models.CASCADE)
    view_down = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.sub.name