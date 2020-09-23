# Generated by Django 3.0.3 on 2020-09-21 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0021_auto_20200922_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='sirketcalisan',
            name='sirket_bilgi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sirket_bilgi', to='sirketapp.Sirket', verbose_name='Şirket Bilgisi'),
        ),
    ]