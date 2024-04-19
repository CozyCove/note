from django.contrib import admin
from .models import note
@admin.register(note)
class noteAdmin(admin.ModelAdmin):
  list_display=['text','created_at']
# Register your models here.
