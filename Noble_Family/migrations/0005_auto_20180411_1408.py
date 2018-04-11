# Generated by Django 2.0.4 on 2018-04-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noble_Family', '0004_auto_20180411_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name_plural': 'Information'},
        ),
        migrations.AlterField(
            model_name='information',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(help_text='Family Name', max_length=20),
        ),
    ]
