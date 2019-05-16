from django.contrib import admin
from .models import Project
from .models import Cursos
from .models import Inscripciones

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
# class CursosAdmin(admin.ModelAdmin):
#     readonly_fields = ('nom')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Cursos)
admin.site.register(Inscripciones)