from django.db import models

# Create your models here.

class dev(models.Model):
    topic = models.TextField(null=True , blank =True)
    session  = models.URLField(max_length = 300 , null=True , blank =True)
    resource = models.TextField(null=True , blank =True)

    def __str__(self):
        return self.topic