# Generated by Django 4.0.1 on 2022-11-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_remove_brand_image_remove_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='images'),
        ),
    ]
