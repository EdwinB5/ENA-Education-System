from django.contrib import admin
from .models import Persona, Profesor, Estudiante
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('nombre', 'apellido', 'dni', 'edad', 'correo', 'telefono', 'created', 'updated')
	search_fields = ('nombre', )
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('año_inicio', 'created', 'updated')
	search_fields = ('nombre',)
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('año_inicio', 'estado', 'created', 'updated')
	search_fields = ('nombre',)
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'