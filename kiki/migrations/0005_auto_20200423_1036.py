# Generated by Django 2.2.12 on 2020-04-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiki', '0004_auto_20200420_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiki',
            name='settibasho',
            field=models.CharField(max_length=30, verbose_name='設置場所'),
        ),
    ]
