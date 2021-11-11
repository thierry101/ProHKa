# Generated by Django 3.2.7 on 2021-09-16 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0017_auto_20210916_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('object', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]