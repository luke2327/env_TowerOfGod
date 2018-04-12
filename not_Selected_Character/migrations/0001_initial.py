# Generated by Django 2.0.4 on 2018-04-12 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='nSelected_Character_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('information_text', models.TextField(default='?')),
                ('detail_information', models.TextField(blank=True, default='', null=True, verbose_name='상세 내용')),
                ('skill', models.TextField(blank=True, default='', null=True, verbose_name='기술')),
                ('position', models.IntegerField(choices=[(1, '파도잡이'), (2, '창지기'), (3, '낚시꾼'), (4, '등대지기'), (5, '탐색꾼'), (6, '불명')], default=1, verbose_name='포지션')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('tag', tagging.fields.TagField(blank=True, max_length=255)),
                ('nSelected_Character_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name_plural': 'Information',
                'ordering': ['created_date'],
            },
        ),
    ]
