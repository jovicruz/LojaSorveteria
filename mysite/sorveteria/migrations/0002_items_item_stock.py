# Generated by Django 4.2 on 2023-05-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorveteria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]