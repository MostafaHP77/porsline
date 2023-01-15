from django.db import models

# Create your models here.
class questionnaire(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class question(models.Model):
    question = models.CharField(max_length=500)
    questionMode = models.CharField(max_length=20)
    questionnaire = models.ForeignKey(questionnaire, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question

class answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text
