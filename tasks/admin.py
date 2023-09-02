from django.contrib import admin
from .models import Task

# Añadimos al panel de Admin la vista de created
class TaskAdmin(admin.ModelAdmin):
    readonly_fields=("created",)
# Register your models here.
admin.site.register(Task, TaskAdmin)