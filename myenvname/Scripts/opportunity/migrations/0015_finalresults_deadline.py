# Generated by Django 3.0 on 2020-04-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0014_finalresults'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalresults',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]