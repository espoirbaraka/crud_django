from django.db import models

# Create your models here.
class Position(models.Model):
    designation = models.CharField(max_length=50)

class Employee(models.Model):
    nom_complet = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    telephone = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
