from django.contrib import admin
from .models import Materia, Grado, Curso, MateriaGrado, GradoCurso, CursoEstudiante
# Register your models here.

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('nombre', 'area', 'created', 'updated')
	search_fields = ('nombre',)
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('numero', 'nivel', 'created', 'updated')
	search_fields = ('numero', 'nivel')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('cupos', 'created', 'updated')
	search_fields = ('cupos',)
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(MateriaGrado)
class MateriaGradoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('grado', 'materia','profesor', 'created', 'updated')
	search_fields = ('materia', 'grado')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(GradoCurso)
class GradoCursoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('grado', 'curso', 'created', 'updated')
	search_fields = ('grado', 'curso')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(CursoEstudiante)
class CursoEstudianteAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('estudiante', 'curso', 'created', 'updated')
	search_fields = ('estudiante', 'curso')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'