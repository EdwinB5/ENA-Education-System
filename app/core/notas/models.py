from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.persona.models import Estudiante
from core.curso.models import Curso
from datetime import datetime

class AñoEscolar(models.Model):
	año = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900), 
                MaxValueValidator(datetime.now().year)],
            help_text='Utiliza el siguiente formato: <YYYY>')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'año escolar'
		verbose_name_plural = 'años escolares'

class Periodo(models.Model):
	numero = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'periodo'
		verbose_name_plural = 'periodos'

class AñoPeriodo(models.Model):
	año = models.ForeignKey(AñoEscolar, on_delete=models.CASCADE)
	periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'año periodo'
		verbose_name_plural = 'años periodos'

class Nota(models.Model):
	nota = models.IntegerField()
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'nota'
		verbose_name_plural = 'notas'

class NotaCurso(models.Model):
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'nota curso'
		verbose_name_plural = 'notas cursos'
