# Generated by Django 5.1.6 on 2025-02-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name_first',
            new_name='name_last',
        ),
    ]
