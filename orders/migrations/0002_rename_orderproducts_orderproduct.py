# Generated by Django 3.2 on 2021-05-14 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210514_2256'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProducts',
            new_name='OrderProduct',
        ),
    ]