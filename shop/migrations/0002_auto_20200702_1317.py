# Generated by Django 3.0.7 on 2020-07-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='rent_date',
            field=models.DateField(auto_now_add=True, verbose_name='Date mise en location'),
        ),
    ]
