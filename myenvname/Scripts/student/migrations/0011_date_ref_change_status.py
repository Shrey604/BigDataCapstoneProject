# Generated by Django 3.0 on 2020-02-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_date_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_ref',
            name='change_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
