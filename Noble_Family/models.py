from django.db import models
from django.utils import timezone
from tagging.fields import TagField
from .choices import *
# Create your models here.

class Information(models.Model):
    class Meta:
        verbose_name_plural = 'Information'
        ordering = ['created_date']
    ## essential info
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                                verbose_name='작성자')
    title = models.CharField(max_length=20, help_text = 'Family Name',
                                verbose_name='가문')
    the_head_of_a_family = models.CharField(max_length=20, verbose_name='가주',
                                            null=True, blank=True)
    information_text = models.TextField(default='?')

    ## relationship floor
    rival_family = models.CharField(max_length=30, default='?')
    friendship_family = models.CharField(max_length=30, default='?')
    sect_family = models.CharField(max_length=30, default='?')
    member_family = models.TextField(default=None, null=True, blank=True)

    ## relationship floor
    dominate_floor = models.CharField(
        max_length=40, default=None, null=True, blank=True)
    origin_family_floor = models.IntegerField(
        default=None, null=True, blank=True)

    ## date settings
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    tag = TagField()

    def __str__(self):
        return self.title

class Information_conceal(models.Model):
    class Meta:
        verbose_name_plural = 'Conceal Information'
        verbose_name = 'Conceal Information'
        ordering = ['created_date']

    ## essential information
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                                verbose_name='작성자')
    title = models.CharField(max_length=20)
    contents_text = models.TextField(null=False, blank=False, default=None)

    ## date settings
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    tag = TagField()

    def __str__(self):
        return self.title

class Noble_Family_Character(models.Model):
    class Meta:
        verbose_name = 'Character'
        ordering = ['created_date']

    ## essential information
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                                verbose_name='작성자')
    title = models.CharField(max_length=20, verbose_name='이름')
    family_name = models.IntegerField(choices=NOBLE_FAMILY_CHOICES, default=1,
                                        verbose_name='가문')
    character_information = models.TextField(default='?', verbose_name='개요')

    ## detail information
    detail_information = models.TextField(default='', null=True,
                                            blank=True, verbose_name='상세 내용')
    skill = models.TextField(default='', null=True, blank=True, verbose_name='기술')
    the_other = models.TextField(default='', null=True, blank=True, verbose_name='기타')

    ## position
    position = models.IntegerField(choices=POSITION_CHOICES, default=1,
                                    verbose_name='포지션')
    advanced_position = models.IntegerField(
        choices=ADVANCED_POSITION_CHOICES, default=0,
        verbose_name='특수 포지션')

    ## date settings
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(default=timezone.now())

    tag = TagField()

    def __str__(self):
        return self.title
