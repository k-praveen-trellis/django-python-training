# Generated by Django 2.0.2 on 2020-02-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200206_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='color',
            field=models.CharField(default='blue', max_length=10),
        ),
    ]
