# Generated by Django 3.0 on 2020-04-09 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_applied_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeddetails',
            name='selectinternshipselected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='completeddetails',
            name='selectplacementselected',
            field=models.BooleanField(default=False),
        ),
    ]
