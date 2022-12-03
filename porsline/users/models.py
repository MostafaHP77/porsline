from django.db import models
from questionnaire.models import questionnaire

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=30)
    questionnaireAnswered = models.ManyToManyField(questionnaire, blank=True)

    def __str__(self):
        return self.name