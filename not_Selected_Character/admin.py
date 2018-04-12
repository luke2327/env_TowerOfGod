from django.contrib import admin
from .models import nSelected_Character_Information
from choices import POSITION_CHOICES

# Register your models here.

class nSelected_Character_Information_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('nSelected_Character_name',
                        'nSelected_Character_information_text',
                        'nSelected_Character_author',)
        }),

        ('Detail Information', {
            'fields': ('nSelected_Character_detail_information',
                        'nSelected_Character_skill',
                        'nSelected_Character_position',
                        'nSelected_Character_source_url', 'tag')
        }),

        ('Date setting', {
            'fields': ('created_date', 'published_date',)
        }),
    )

    search_fields = ('nSelected_Character_name',)
    list_filter = ('created_date',)
    list_display = ('nSelected_Character_name', 'id',
                     'nSelected_Character_position',
                     'created_date', 'nSelected_Character_author', 'tag')
    list_per_page = 20

admin.site.register(nSelected_Character_Information,
                    nSelected_Character_Information_Admin)
