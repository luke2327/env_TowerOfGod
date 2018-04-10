from django.contrib import admin
from .models import Noble_Family_information
# Register your models here.

class Noble_Family_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('title', 'information_text', 'author')
        }),

        ('Advanced options', {
            'fields': ('member_family', 'friendship_family', 'rival_family',
                        'sect_family', 'dominate_floor', 'origin_family_floor',)
        }),
    )

    search_fields = ('title',)

admin.site.register(Noble_Family_information, Noble_Family_Admin)
