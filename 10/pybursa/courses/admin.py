from django.contrib import admin

from .models import Course, Address
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail','slug', 'assistent', 'prepod')
    ordering = ('slug', 'name')
    search_fields = ('name', 'prepod')
    list_filter = ['prepod', 'start']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Address)