# Generated by Django 5.0.4 on 2024-07-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_rangi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('aboute', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
