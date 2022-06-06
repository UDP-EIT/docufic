from django.contrib import admin
# Cambiar esto por los modelos que se usan por el amor de dios
from .models import *

# Funciones complementarias para registro


class VerSeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion')


class VerEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('archivo', 'ramo', 'tipo', 'anyo', 'semestre')


class VerMaterialAdmin(admin.ModelAdmin):
    list_display = ('archivo', 'ramo', 'autor')


class VerRamoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'subseccion', 'numero_evaluaciones')


class VerBuscadorPatchAdmin(admin.ModelAdmin):
    list_display = ('nombre_alternativo', 'ramo')


# Prototipo panel de administración
admin.site.register(Seccion)
admin.site.register(Subseccion, VerSeccionAdmin)
admin.site.register(Ramo, VerRamoAdmin)
admin.site.register(Evaluacion, VerEvaluacionAdmin)
admin.site.register(Material, VerMaterialAdmin)
admin.site.register(TiposDeMaterial)
admin.site.register(BuscadorPatch, VerBuscadorPatchAdmin)