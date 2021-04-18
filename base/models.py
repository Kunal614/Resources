from django.db import models

# Create your models here.
class about(models.Model):
    data = models.TextField(null=True , blank = True )

class details(models.Model):
    name = models.CharField(max_length = 200 ,null=True , blank = True)
    email = models.EmailField(null=True , blank = True)
    description = models.TextField(null=True , blank = True)

    def __str__(self):
        return self.name