# Generated by Django 4.0.4 on 2022-05-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_photogallery_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_per_serving',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
