# Generated by Django 3.0 on 2020-02-21 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200221_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='postionofinterest',
            new_name='positionofinterest',
        ),
    ]