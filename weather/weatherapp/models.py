#weatherapp/models
from django.db import models

# Create your models here.
class citymodel(models.Model):
    city=models.CharField(max_length=100,default='bogota')

    def __str__(self):
        return self.city