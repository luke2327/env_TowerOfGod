# Generated by Django 2.0.4 on 2018-04-11 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FUG', '0006_auto_20180410_2001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'Character'},
        ),
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name_plural': 'Information'},
        ),
    ]
