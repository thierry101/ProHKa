# Generated by Django 2.2.20 on 2021-11-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0030_auto_20211116_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='authenticated',
            field=models.BooleanField(default=True),
        ),
    ]