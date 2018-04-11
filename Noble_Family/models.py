from django.db import models
from django.utils import timezone
from tagging.fields import TagField
# Create your models here.

class Information(models.Model):
    class Meta:
        verbose_name_plural = 'Information'
    ## essential info
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, help_text = 'Family Name')
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

    ## essential information
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    contents_text = models.TextField(null=False, blank=False, default=None)

    ## date settings
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    tag = TagField()

    def __str__(self):
        return self.title
