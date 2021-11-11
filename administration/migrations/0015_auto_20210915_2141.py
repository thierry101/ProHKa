# Generated by Django 3.2.7 on 2021-09-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0014_auto_20210915_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsetting',
            name='aboutUs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='localisation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='status',
            field=models.BooleanField(default=False, unique=True),
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]