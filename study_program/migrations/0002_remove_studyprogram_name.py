# Generated by Django 2.0.2 on 2018-10-06 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyprogram',
            name='name',
        ),
    ]
