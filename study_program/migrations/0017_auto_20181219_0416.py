# Generated by Django 2.1.2 on 2018-12-18 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0016_auto_20181219_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aun',
            name='assessment_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='study_program.AssessmentResult'),
        ),
    ]
