from django.db import models
from core.persona.models import Profesor, Estudiante

# Create your models here.

class Materia(models.Model):
	nombre = models.CharField(max_length=50) 
	area = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'materia'
		verbose_name_plural = 'materias'

	def __str__(self):
		return self.nombre

class Grado(models.Model):
	numero = models.IntegerField()
	nivel = models.CharField(max_length=25)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'grado'
		verbose_name_plural = 'grados'

class Curso(models.Model):
	cupos = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'curso'
		verbose_name_plural = 'cursos'

class MateriaGrado(models.Model):
	grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'materia grado'
		verbose_name_plural = 'materias grados'

class GradoCurso(models.Model):
	grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'grado curso'
		verbose_name_plural = 'grados cursos'

class CursoEstudiante(models.Model):
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'curso estudiante'
		verbose_name_plural = 'cursos estudiantes'