# Generated by Django 5.0.4 on 2024-06-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]