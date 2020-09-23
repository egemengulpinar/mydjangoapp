# Generated by Django 3.0.3 on 2020-09-10 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aracsoforapp', '0003_auto_20200910_1602'),
        ('transferapp', '0007_auto_20200825_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='arac',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arac', to='aracsoforapp.AracModel', verbose_name='Araç Modeli'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='sofor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sofor', to='aracsoforapp.AracSofor', verbose_name='Şöför'),
        ),
    ]