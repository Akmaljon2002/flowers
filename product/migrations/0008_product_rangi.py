# Generated by Django 5.0.4 on 2024-06-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_qonish_joyi_product_sotib_olish_turi'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rangi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]