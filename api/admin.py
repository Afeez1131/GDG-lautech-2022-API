from django.contrib import admin
from .models import Attendees


@admin.register(Attendees)
class AttendeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'interest', 'phone', 'email']
