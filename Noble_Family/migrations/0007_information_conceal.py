# Generated by Django 2.0.4 on 2018-04-11 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Noble_Family', '0006_auto_20180411_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information_conceal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('contents_text', models.TextField(default=None)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', tagging.fields.TagField(blank=True, max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Conceal Information',
            },
        ),
    ]
