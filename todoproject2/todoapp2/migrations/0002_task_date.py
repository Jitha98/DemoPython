# Generated by Django 4.2.4 on 2023-08-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-22'),
            preserve_default=False,
        ),
    ]
