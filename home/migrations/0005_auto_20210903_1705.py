# Generated by Django 3.2.7 on 2021-09-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_settings_actif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slide1', models.ImageField(blank=True, null=True, upload_to='SettingsImg/Logo', verbose_name='Slide1')),
                ('slide2', models.ImageField(blank=True, null=True, upload_to='SettingsImg/Logo', verbose_name='Slide2')),
                ('slide3', models.ImageField(blank=True, null=True, upload_to='SettingsImg/Logo', verbose_name='Slide3')),
                ('actif', models.BooleanField(default=False, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='settings',
            name='slide1',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='slide2',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='slide3',
        ),
    ]