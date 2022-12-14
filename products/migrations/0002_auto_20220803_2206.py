# Generated by Django 3.2.14 on 2022-08-04 01:06

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=1, upload_to=products.models.upload_image_products),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
