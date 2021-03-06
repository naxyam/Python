from django.db import models

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    direccion=models.CharField(max_length = 50, verbose_name='La dirección')
    email= models.EmailField(blank= True, null=True)
    tfono= models.CharField(max_length=7)

    def __str__(self):
    	return self.nombre


class Articulo(models.Model):
 	nombre=models.CharField(max_length=30)
 	seccion=models.CharField(max_length = 20)
 	precio = models.IntegerField()

 	def __str__(self):
 		return 'El nombre es %s la sección es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
 	numero=models.IntegerField()
 	fecha=models.DateField()
 	entregado = models.BooleanField()
