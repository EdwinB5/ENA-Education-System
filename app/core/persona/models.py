from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	dni = models.IntegerField()
	edad = models.IntegerField()
	correo = models.EmailField(blank=True, null=True)
	telefono = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'persona'
		verbose_name_plural = 'personas'

	def __str__(self):
		return self.nombre

class Profesor(models.Model):
	nombre = models.ForeignKey(Persona, on_delete=models.CASCADE)
	año_inicio = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'profesor'
		verbose_name_plural = 'profesores'

	def __str__(self):
		return self.nombre

class Estudiante(models.Model):
	nombre = models.ForeignKey(Persona, on_delete=models.CASCADE)
	año_inicio = models.DateField()
	estado = models.BooleanField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'estudiante'
		verbose_name_plural = 'estudiantes'

	def __str__(self):
		return self.nombre