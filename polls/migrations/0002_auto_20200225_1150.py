# Generated by Django 3.0.3 on 2020-02-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]