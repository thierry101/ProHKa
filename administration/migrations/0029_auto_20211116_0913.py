# Generated by Django 2.2.20 on 2021-11-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0028_evaluationfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationfile',
            name='userId',
        ),
        migrations.AddField(
            model_name='evaluationfile',
            name='decision',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
