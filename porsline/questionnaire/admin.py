from django.contrib import admin
from questionnaire.models import questionnaire, question, answer

# Register your models here.
admin.site.register(questionnaire)
admin.site.register(question)
admin.site.register(answer)