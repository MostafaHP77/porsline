from django.urls import path
from questionnaire.views import questionnaires

urlpatterns = [
    path('list/', questionnaires, name='questionnaire')
]
