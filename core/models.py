from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER = [("Male", "Male"), ("Female", "Female")]
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    age = models.IntegerField(validators=[
            MaxValueValidator(100), # gt
            MinValueValidator(1) # lt
        ],null=True)
    gender = models.CharField(choices=GENDER,null=True,max_length=10)


