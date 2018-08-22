from django.contrib import admin

# Register your models here.
from .models import Coache, Dossier


class CoacheAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','email', 'role', 'user')
    ordering = ('role', 'name')
    search_fields = ('name', 'email')
    list_filter = ['email', 'user']
    radio_fields = {"role": admin.HORIZONTAL}



admin.site.register(Coache, CoacheAdmin)
admin.site.register(Dossier)