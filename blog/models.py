from datetime import date
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=190)
    subject = models.CharField(max_length=120)
    date = models.DateField(default=date.today)
    deiscription = models.TextField(null=True, blank=True)
    
   



# Create your models here.
