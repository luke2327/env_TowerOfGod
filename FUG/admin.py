from django.contrib import admin
from .models import Character, Information
from django.db.models import Q

# Register your models here.
class FUG_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('title', 'text', 'author',)
        }),

        ('Advanced options', {
            'fields': ('created_date', 'published_date', 'generation', 'post_position'),
        })
    )
    list_display = (
        'title', 'id', 'post_position', 'text', 'author', 'created_date'
    )
    list_filter = ('author',)
    search_fields = ('title',)
    ordering = ('created_date',)

    list_per_page = 20
    list_filter = ('created_date',)

class Information_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Outline', {
            'fields': ('title', 'information',)
        }),
    )
    list_display = (
        'title',
    )
admin.site.register(Character, FUG_Admin)
admin.site.register(Information, Information_Admin)
