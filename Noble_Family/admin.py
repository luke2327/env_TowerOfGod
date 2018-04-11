from django.contrib import admin
from .models import Information, Information_conceal, \
    Noble_Family_Character
# Register your models here.

class Noble_Family_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('title', 'the_head_of_a_family',
                        'information_text', 'author')
        }),

        ('Advanced options', {
            'fields': ('member_family', 'friendship_family',
                        'rival_family', 'sect_family',
                        'dominate_floor', 'origin_family_floor',
                        'tag')
        }),

        ('Date setting', {
            'fields': ('created_date', 'published_date')
        }),
    )

    search_fields = ('title',)
    list_filter = ('created_date',)
    list_display = ('title', 'id', 'the_head_of_a_family',
                     'created_date', 'author', 'tag')

    list_per_page = 20

class Noble_Family_Information_conceal_Admin(admin.ModelAdmin):
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

    list_display = ('title', 'id', 'created_date', 'author', 'tag')
    list_filter = ('created_date',)

class Noble_Family_Character_Admin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': ('title', 'character_information',
                        'family_name', 'author')
        }),

        ('Detail information', {
            'fields': ('position', 'advanced_position',
                        'detail_information', 'skill')
        }),

        ('Supplement', {
            'fields': ('the_other', 'tag')
        }),

        ('Date setting', {
            'fields': ('created_date', 'published_date')
        }),
    )

    list_display = ('title', 'family_name',
                     'position', 'tag', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('title',)

admin.site.register(Information, Noble_Family_Admin)
admin.site.register(
    Information_conceal, Noble_Family_Information_conceal_Admin)
admin.site.register(
    Noble_Family_Character, Noble_Family_Character_Admin)
