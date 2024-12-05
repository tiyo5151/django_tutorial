from django.contrib import admin
from .models import Page

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]
