# Generated by Django 2.0.4 on 2018-04-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('not_Selected_Character', '0004_remove_nselected_character_information_nselected_character_source_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='nselected_character_information',
            name='nSelected_Character_source_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='source url'),
        ),
    ]
