# Generated by Django 2.0.4 on 2018-04-12 07:31

import datetime
from django.db import migrations, models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('not_Selected_Character', '0008_auto_20180412_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='nSelected_Character_Detail_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nSelected_Character_Detail_Information_title', models.CharField(max_length=30, verbose_name='제목')),
                ('nSelected_Character_Detail_Information_text', models.TextField(blank=True, default='', null=True, verbose_name='내용')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 4, 12, 16, 31, 18, 335298))),
                ('published_date', models.DateTimeField(default=datetime.datetime(2018, 4, 12, 16, 31, 18, 335298))),
                ('tag', tagging.fields.TagField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Information',
            },
        ),
        migrations.AlterField(
            model_name='nselected_character_list',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 12, 16, 31, 18, 334797)),
        ),
        migrations.AlterField(
            model_name='nselected_character_list',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 12, 16, 31, 18, 334797)),
        ),
    ]
