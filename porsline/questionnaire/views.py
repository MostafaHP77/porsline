# from django.shortcuts import render
# from questionnaire.models import questionnaire
# from django.http import JsonResponse

# # Create your views here.

# def questionnaires(request):
#     questionnaires = questionnaire.objects.all()
#     # print(questionnaires.values())
#     data = {
#         'questionnaires': list(questionnaires.values())
#     }
#     print(type(list(questionnaires.values())))
#     return JsonResponse(data)
