from django.db import models

# Create your models here.
class Familia(models.Model):
    
    familiar= models.CharField(max_length=20, default="familiar")
    nombre= models.CharField(max_length=30, default= "preguntar")
    edad= models.IntegerField(default= "preguntar")

