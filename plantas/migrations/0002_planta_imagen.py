# Generated by Django 4.0.5 on 2023-06-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]