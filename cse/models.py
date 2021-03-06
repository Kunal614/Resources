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


class Books(models.Model):
    subj = models.ForeignKey(subject, on_delete=models.CASCADE)
    book_name = models.CharField(max_length = 200 , default="NA")
    view_down = models.URLField(max_length = 200 , null=True , blank = True)
    def __str__(self):
        return self.subj.name

class Other_stuff(models.Model):
    subj = models.ForeignKey(subject, on_delete=models.CASCADE)
    other_name = models.CharField(max_length = 200 , default="NA")
    view_down = models.URLField(max_length = 200 ,  null=True , blank = True)
    def __str__(self):
        return self.subj.name

       