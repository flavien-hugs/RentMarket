# Generated by Django 3.0.8 on 2020-07-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_productmodel_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='featured',
            field=models.BooleanField(default=True, verbose_name='En vedette'),
        ),
    ]
