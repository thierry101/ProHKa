# Generated by Django 2.2.20 on 2021-10-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0023_auto_20211021_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='todo',
        ),
        migrations.AddField(
            model_name='userregistration',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='chlildren',
            field=models.IntegerField(blank=True, null=True, verbose_name="Nombre d'enfants"),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='religion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Religion'),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='situation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Situation matrimoniale'),
        ),
    ]