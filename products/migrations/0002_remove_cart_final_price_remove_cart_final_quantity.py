# Generated by Django 4.2.5 on 2023-09-13 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='final_price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='final_quantity',
        ),
    ]