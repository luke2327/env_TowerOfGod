from django.contrib import admin
from .models import nSelected_Character_Information, \
                    nSelected_Character_List, \
                    nSelected_Character_Detail_Information
from choices import POSITION_CHOICES
from exportCsv import ExportCsvMixin

@admin.register(nSelected_Character_Information)
class nSelected_Character_Information_Admin(admin.ModelAdmin, ExportCsvMixin):
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
    actions = ['export_as_csv']
    list_per_page = 20

@admin.register(nSelected_Character_List)
class nSelected_Character_List_Admin(admin.ModelAdmin, ExportCsvMixin):
    fieldsets = (
        ('Information', {
            'fields': ('nSelected_Character_name',
                       'nSelected_Character_Class',
                       'nSelected_Character_Rank',)
        }),
        ('Date setting', {
            'fields': ('created_date', 'published_date',)
        }),
    )

    search_fields = ('nSelected_Character_name',)
    list_filter = ('created_date',)
    list_display = ('nSelected_Character_name',
                    'nSelected_Character_Rank',
                    'nSelected_Character_Class')
    actions = ['export_as_csv']

@admin.register(nSelected_Character_Detail_Information)
class nSelected_Character_Detail_Information_Admin(admin.ModelAdmin, ExportCsvMixin):
    fieldsets = (
        ('Information', {
            'fields': ('nSelected_Character_Detail_Information_title',
                       'nSelected_Character_Detail_Information_text', 'tag')
        }),
        ('Date setting', {
            'fields': ('created_date', 'published_date',)
        }),
    )

    search_fields = ('nSelected_Character_Detail_Information_title',)
    list_filter = ('created_date',)
    list_display = ('nSelected_Character_Detail_Information_title',
                    'tag', 'created_date')
    actions = ['export_as_csv']
