# Generated by Django 2.2.20 on 2021-11-04 14:49

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20211025_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='civility',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]
