from django.contrib import admin

# Register your models here.

from escola.models import ALuno


class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(ALuno, Alunos)
