# Generated by Django 4.2.5 on 2023-10-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_rename_receipe_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='vege/recipe'),
        ),
    ]
