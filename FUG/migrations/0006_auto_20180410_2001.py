# Generated by Django 2.0.4 on 2018-04-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FUG', '0005_auto_20180410_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='post_position',
            field=models.CharField(default='?', max_length=30, null=True, verbose_name='직위'),
        ),
        migrations.AlterField(
            model_name='character',
            name='text',
            field=models.TextField(default='?', verbose_name='이명'),
        ),
        migrations.AlterField(
            model_name='character',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='information',
            name='information',
            field=models.TextField(),
        ),
    ]