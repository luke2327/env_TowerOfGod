from django.contrib import admin
from .models import Character

# Register your models here.
class FUG_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Infomation', {
            'fields': ('title', 'text', 'author',)
        }),
        ('Advanced options', {
            'fields': ('id', 'created_date', 'published_date', 'generation', 'post_position'),
        })
    )
    list_display = (
        'title', 'id', 'text', 'post_position', 'author', 'created_date'
    )
    list_filter = ('author',)
    search_fields = ('title',)
    ordering = ('created_date',)

    list_per_page = 20
    
admin.site.register(Character, FUG_Admin)
