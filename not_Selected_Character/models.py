from django.db import models
from django.utils import timezone
from tagging.fields import TagField
from django.core.validators import URLValidator
from choices import *
from django import forms

# Create your models here.
class nSelected_Character_Information(models.Model):
    class Meta:
        verbose_name_plural = 'Characters'
        # ordering = ['created_date']

    ## essential info
    nSelected_Character_author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='작성자')
    nSelected_Character_name = models.CharField(
        max_length=20, verbose_name='이름')
    nSelected_Character_information_text = models.TextField(
        default='?', verbose_name='정보')

    ## detail information
    nSelected_Character_detail_information = models.TextField(
        default='', null=True, blank=True, verbose_name='상세 내용')
    nSelected_Character_skill = models.TextField(
        default='', null=True, blank=True, verbose_name='기술')

    ## position
    nSelected_Character_position = models.IntegerField(
        choices=POSITION_CHOICES, default=1, verbose_name='포지션')

    ## date settings
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    tag = TagField()
    nSelected_Character_source_url = models.CharField(
        max_length=255, blank=True, null=True, default='',
        verbose_name='source url')


    def __str__(self):
        return self.nSelected_Character_name
