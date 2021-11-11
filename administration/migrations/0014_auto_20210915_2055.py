# Generated by Django 3.2.7 on 2021-09-15 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0013_globalsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsetting',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='globalsetting',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
