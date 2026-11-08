from django.db import models

# Create your models here.
class Person1(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.first_name}object created"