# Generated by Django 2.0 on 2018-02-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommate', '0003_newroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newroom',
            name='Maximum_Participants',
            field=models.IntegerField(),
        ),
    ]
