
from django.contrib import admin
from .models import Udhiyah

@admin.register(Udhiyah)
class UdhiyahAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'donation_type', 'status', 'updated_at')
    list_filter = ('status', 'donation_type')
    search_fields = ('id', 'name', 'phone')
