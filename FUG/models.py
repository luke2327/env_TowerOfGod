from django.db import models
from django.utils import timezone
# Create your models here.

class Character(models.Model):
    # obj = Character.objects.get(pk=this_object_id)
    # id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField(default='?', verbose_name='이명')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    generation = models.IntegerField(default=1, blank=True)
    post_position = models.CharField(max_length=30, null=True, default='?', verbose_name='직위')

    # @property
    # def category_id(self):
    #     return self.id

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
class Information(models.Model):
    title = models.CharField(max_length=20)
    information = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
