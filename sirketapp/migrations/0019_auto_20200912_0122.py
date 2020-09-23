# Generated by Django 3.0.3 on 2020-09-11 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0018_auto_20200912_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirket',
            name='created_date',
            field=models.DateTimeField(null=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='sirket',
            name='sirket_no',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Şirket Tel No'),
        ),
    ]