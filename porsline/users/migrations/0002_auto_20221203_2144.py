# Generated by Django 3.2 on 2022-12-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_alter_questionnaire_name'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='questionnaireAnswered',
            field=models.ManyToManyField(null=True, to='questionnaire.questionnaire'),
        ),
    ]