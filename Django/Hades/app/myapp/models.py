from django.db import models

class Employee(models.Model):
	nombre= models.CharField(max_length=150, verbose_name='Nombres')
	DBU= models.CharField(max_length=10,unique=True, )

