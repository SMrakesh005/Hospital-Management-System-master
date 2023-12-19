# Generated by Django 3.0.5 on 2023-03-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0033_remove_patient_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='prescription',
            field=models.CharField(default='--', max_length=500),
        ),
        migrations.AddField(
            model_name='patient',
            name='tests',
            field=models.CharField(default='--', max_length=100),
        ),
    ]