# Generated by Django 2.1.2 on 2018-10-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0014_aun_assessment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aun',
            name='assessment_id',
        ),
    ]