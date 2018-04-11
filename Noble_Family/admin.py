from django.contrib import admin
from .models import Information, Information_conceal
# Register your models here.

class Noble_Family_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('title',
                        'the_head_of_a_family', 'information_text', 'author')
        }),

        ('Advanced options', {
            'fields': ('member_family', 'friendship_family', 'rival_family',
                        'sect_family', 'dominate_floor', 'origin_family_floor', 'tag')
        }),

        ('Date setting', {
            'fields': ('created_date', 'published_date')
        }),
    )

    search_fields = ('title',)
    list_filter = ('created_date',)

    list_per_page = 20

class Noble_Family_Information_conceal(admin.ModelAdmin):
    fieldsets = (
        ('Basic Contents', {
            'fields': ('title', 'contents_text', 'author')
        }),

        ('Advanced options', {
            'fields': ('tag',)
        }),

        ('Date setting', {
            'fields': ('created_date', 'published_date')
        }),
    )

    list_filter = ('created_date',)

admin.site.register(Information, Noble_Family_Admin)
admin.site.register(Information_conceal, Noble_Family_Information_conceal)
