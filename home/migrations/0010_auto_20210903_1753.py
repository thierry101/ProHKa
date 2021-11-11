# Generated by Django 3.2.7 on 2021-09-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210903_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='actif',
            field=models.BooleanField(default=False, unique=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Promotion1'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Promotion2'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Promotion3'),
        ),
    ]
