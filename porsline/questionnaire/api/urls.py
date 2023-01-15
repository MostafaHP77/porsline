from django.urls import path
from questionnaire.api.views import questionnairesList

urlpatterns = [
    path('', questionnairesList.as_view(), name='questionnaire'),
    # path('add/', questionnairesList., name='questionnaireById'),
    # path('', questionnaire, name='questionnaireByName')
]
