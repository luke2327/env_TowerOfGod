from django.db import models
from django.utils import timezone
# Create your models here.

class Noble_Family_information(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    information_text = models.TextField(default='?')
    rival_family = models.CharField(max_length=30, default='?')
    friendship_family = models.CharField(max_length=30, default='?')
    sect_family = models.CharField(max_length=30, default='?')
    dominate_floor = models.CharField(max_length=40, default=None, null=True, blank=True)
    member_family = models.TextField(default=None, null=True, blank=True)
    origin_family_floor = models.IntegerField(max_length=135, default=None, null=True, blank=True)
    # tag = models.ManyToManyField()
