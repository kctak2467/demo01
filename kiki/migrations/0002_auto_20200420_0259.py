# Generated by Django 2.2.12 on 2020-04-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiki',
            name='juyodo',
            field=models.CharField(max_length=2),
        ),
    ]
