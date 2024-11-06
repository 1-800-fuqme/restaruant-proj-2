from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=35)
    phone_number=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.username}"

class Recipes(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    ingredients=models.TextField()
    prep_time_min=models.IntegerField()
    instructions=models.TextField()
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name} {self.prep_time_min}"
