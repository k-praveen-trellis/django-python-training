# Generated by Django 2.0.2 on 2020-02-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
    ]
