# Generated by Django 3.0.3 on 2020-02-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_questions_question_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]