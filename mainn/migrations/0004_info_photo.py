# Generated by Django 4.0.2 on 2022-02-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0003_info_alter_mainimg_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mainn/infoImg/', verbose_name='Фото'),
        ),
    ]