# Generated by Django 5.0.2 on 2024-03-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
