# Generated by Django 5.0.4 on 2024-06-05 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]