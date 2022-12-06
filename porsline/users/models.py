from django.db import models
from questionnaire.models import questionnaire, answer

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=30)
    questionnaireAnswered = models.ManyToManyField(questionnaire, blank=True)

    def __str__(self):
        return self.name

class userAnswer(models.Model):
    answer = models.ForeignKey(answer, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('answer', 'user',)

    def __str__(self):
        return str(self.user.id) + ':' + self.answer.text