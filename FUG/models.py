from django.db import models
from django.utils import timezone
# Create your models here.

class Character(models.Model):
    class Meta:
        verbose_name = 'Character'

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                                verbose_name='작성자')
    title = models.CharField(max_length=20, verbose_name='이름')
    text = models.TextField(default='?', verbose_name='이명')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    generation = models.IntegerField(default=1, blank=True)
    post_position = models.CharField(
        max_length=30, null=True, default='?', verbose_name='직위')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
        
class Information(models.Model):
    class Meta:
        verbose_name_plural = 'Information'
    title = models.CharField(max_length=20)
    information = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
