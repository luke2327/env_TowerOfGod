# Generated by Django 2.0.4 on 2018-04-11 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Noble_Family', '0009_auto_20180411_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='noble_family_character',
            name='detail_information',
            field=models.TextField(default='?', verbose_name='상세 내용'),
        ),
        migrations.AddField(
            model_name='noble_family_character',
            name='skill',
            field=models.TextField(blank=True, default='', null=True, verbose_name='기술'),
        ),
        migrations.AddField(
            model_name='noble_family_character',
            name='the_other',
            field=models.TextField(blank=True, default='', null=True, verbose_name='기타'),
        ),
        migrations.AlterField(
            model_name='noble_family_character',
            name='advanced_position',
            field=models.IntegerField(choices=[(1, '---------'), (2, '길잡이'), (3, '디펜더'), (4, '단술사'), (5, '원술사'), (6, '전술사'), (7, '주술사'), (8, '화염사'), (9, '부리미')], default=0, verbose_name='특수 포지션'),
        ),
        migrations.AlterField(
            model_name='noble_family_character',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 9, 15, 7, 776077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noble_family_character',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 9, 15, 7, 776077, tzinfo=utc)),
        ),
    ]
