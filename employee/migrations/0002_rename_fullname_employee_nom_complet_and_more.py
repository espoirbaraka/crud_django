# Generated by Django 4.0.4 on 2022-07-26 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='fullname',
            new_name='nom_complet',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='mobile',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='title',
            new_name='designation',
        ),
    ]