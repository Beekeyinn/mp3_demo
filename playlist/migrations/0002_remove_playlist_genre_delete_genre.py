# Generated by Django 4.0.3 on 2022-04-08 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]