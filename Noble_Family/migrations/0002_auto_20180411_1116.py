# Generated by Django 2.0.4 on 2018-04-11 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Noble_Family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noble_family_information',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='noble_family_information',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='noble_family_information',
            name='member_family',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='noble_family_information',
            name='origin_family_floor',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]