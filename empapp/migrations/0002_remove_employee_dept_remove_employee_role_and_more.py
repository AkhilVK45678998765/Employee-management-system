# Generated by Django 4.1.5 on 2023-02-28 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
