# Generated by Django 3.0 on 2020-02-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0002_auto_20200223_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipopportunity',
            name='encode_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='internshipplusplacementopportunity',
            name='encode_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='placementopportunity',
            name='encode_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
