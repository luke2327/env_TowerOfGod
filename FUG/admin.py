from django.contrib import admin
from .models import Character, Information
from django.db.models import Q
from exportCsv import ExportCsvMixin

# Register your models here.

@admin.register(Character)
class FUG_Admin(admin.ModelAdmin, ExportCsvMixin):
    fieldsets = (
        ('Information', {
            'fields': ('title', 'text', 'author',)
        }),

        ('Advanced options', {
            'fields': ('created_date', 'published_date',
                       'generation', 'post_position'),
        })
    )
    list_display = (
        'title', 'id', 'post_position', 'text', 'created_date', 'author',
    )
    list_filter = ('author',)
    search_fields = ('title',)
    ordering = ('created_date',)
    actions = ['export_as_csv']

    list_per_page = 20
    list_filter = ('created_date',)

@admin.register(Information)
class Information_Admin(admin.ModelAdmin, ExportCsvMixin):
    fieldsets = (
        ('Outline', {
            'fields': ('title', 'information',)
        }),
    )
    list_display = (
        'title',
    )

    actions = ['export_as_csv']
