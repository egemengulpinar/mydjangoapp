# Generated by Django 3.0.3 on 2020-08-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0009_auto_20200823_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirket',
            name='created_date',
            field=models.DateField(null=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]