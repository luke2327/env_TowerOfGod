# Generated by Django 2.0.4 on 2018-04-12 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('not_Selected_Character', '0003_auto_20180412_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nselected_character_information',
            name='nSelected_Character_source_url',
        ),
    ]
