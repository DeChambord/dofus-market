# Generated by Django 5.0.6 on 2024-06-10 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='_prix',
            new_name='prix',
        ),
    ]