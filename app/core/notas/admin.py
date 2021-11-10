from django.contrib import admin
from .models import AñoEscolar, Periodo, AñoPeriodo, Nota, NotaCurso
# Register your models here.

@admin.register(AñoEscolar)
class AñoEscolarAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('año', 'created', 'updated')
	search_fields = ('año', )
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('numero', 'created', 'updated')
	search_fields = ('numero', )
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(AñoPeriodo)
class AñoPeriodoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('año', 'periodo', 'created', 'updated')
	search_fields = ('año', 'periodo')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('nota', 'estudiante', 'periodo', 'created', 'updated')
	search_fields = ('año', 'estudiante', 'periodo')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'

@admin.register(NotaCurso)
class NotaCursoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('curso', 'nota', 'created', 'updated')
	search_fields = ('nota', 'curso')
	list_filter = ('created', 'updated')
	date_hierarchy = 'created'