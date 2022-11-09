from django.contrib import admin
from .models import ShowData

@admin.register(ShowData)
class ShowDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')