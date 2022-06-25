from django.contrib import admin
from apps.computer.models import ComputerModel


@admin.register(ComputerModel)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'ram', 'display_size')
