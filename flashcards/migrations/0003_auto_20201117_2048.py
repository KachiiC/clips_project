# Generated by Django 3.1.3 on 2020-11-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_auto_20201117_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubeclip',
            name='end_stamp',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='youtubeclip',
            name='start_stamp',
            field=models.IntegerField(blank=True),
        ),
    ]
