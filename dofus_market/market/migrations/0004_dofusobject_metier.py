# Generated by Django 5.0.6 on 2024-06-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_rename__prix_ba_rune_prix_ba_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dofusobject',
            name='metier',
            field=models.CharField(default='cordonnier', max_length=100),
            preserve_default=False,
        ),
    ]
