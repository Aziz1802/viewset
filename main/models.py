from django.db import models

# Create your models here.


class Student(models.Model):
    DIRECTIONS = (
        ('Back-end','Back-end'),
        ('Front-end','Front-end'),
        ('Fullstack','Fullstack'),
        ('UX/Ui','UX/UI')
    )
    DIRECTIONS2=(
        ('male','male'),
        ('female','female')
    )
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    direction = models.CharField(max_length=255,choices=DIRECTIONS)
    gender = models.CharField(max_length=255,choices=DIRECTIONS2)