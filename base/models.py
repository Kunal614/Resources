from django.db import models
import datetime

# Create your models here.
class about(models.Model):
    data = models.TextField(null=True , blank = True )

class details(models.Model):
    name = models.CharField(max_length = 200 ,null=True , blank = True)
    email = models.EmailField(null=True , blank = True)
    description = models.TextField(null=True , blank = True)
    date = models.DateField(blank=True, null=True )

    def __str__(self):
        return str(self.date)

class tokenStuff(models.Model):
    access_token = models.TextField(null=True , blank = True)
    time = models.TimeField(null = True , blank = True)
    date = models.DateField(null = True , blank = True)
    refresh_token = models.TextField(null = True , blank = True)
    expires_in = models.IntegerField(null = True , blank = True)


class notification(models.Model):
    notify = models.TextField(null = True , blank =True)