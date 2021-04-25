from django.db import models

# Create your models here.
class cp(models.Model):
    title = models.TextField(null=True , blank = True)
    data = models.TextField(null=True , blank = True)
    question = models.TextField(null=True , blank = True)
    
    def __str__(self):
        return self.title
    

class problemofday(models.Model):
    problem_of_the_day = models.URLField(max_length = 300 , null=True , blank =True)
    old_questions = models.TextField(null=True , blank =True)
    ratings = models.CharField(max_length = 100 , default =1200)
    tags = models.CharField(max_length = 200 , default = 'implementation')

    def __str__(self):
        return self.tags

class problemset(models.Model):
    url = models.URLField(max_length = 300 , null=True , blank =True)
    date_of_problem = models.DateField(null=True , blank =True)
    tags = models.TextField(null=True , blank =True)
    ratings = models.CharField(max_length = 100 , default =1200)
    name = models.CharField(max_length = 200 , null = True , blank =True)

    def __str__(self):
        return str(self.name)
