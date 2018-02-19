# Generated by Django 2.0 on 2018-02-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('Entry_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Entry_Made_By', models.CharField(max_length=20)),
                ('Entry_Date', models.DateTimeField()),
                ('Amount', models.IntegerField()),
                ('Description', models.TextField(max_length=500)),
            ],
        ),
    ]
