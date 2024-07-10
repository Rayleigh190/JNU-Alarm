# Generated by Django 5.0.1 on 2024-07-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortcuts',
            old_name='image_name',
            new_name='aos_image_name',
        ),
        migrations.AddField(
            model_name='shortcuts',
            name='ios_image_name',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]
