from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from alumno.resources import AlumnoResource


# class AlumnoAdmin(admin.ModelAdmin):
class AlumnoAdmin(ImportExportModelAdmin):
    list_display = ('alumnx', 'curso', 'generacion', 'email',
                    'pais', 'bio', 'codigo', 'clave')
    readonly_fields = ('fecha_inscripcion',)
    list_per_page = 25
    resource_class = AlumnoResource


admin.site.register(Alumno, AlumnoAdmin)
