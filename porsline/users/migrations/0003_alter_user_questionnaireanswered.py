# Generated by Django 3.2 on 2022-12-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_alter_questionnaire_name'),
        ('users', '0002_auto_20221203_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='questionnaireAnswered',
            field=models.ManyToManyField(blank=True, to='questionnaire.questionnaire'),
        ),
    ]
