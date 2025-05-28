
from django.contrib import admin
from .models import Udhiyah

@admin.register(Udhiyah)
class UdhiyahAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'updated_at')
    list_filter = ('status',)
    search_fields = ('id', 'name', 'phone')
