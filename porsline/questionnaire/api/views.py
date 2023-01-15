from questionnaire.models import questionnaire, question, answer
from questionnaire.api.serializers import questionnaireSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

class questionnairesList(APIView):
    def get(self, request):
        questionnaires = questionnaire.objects.all()
        serializedData = questionnaireSerializer(questionnaires, many=True)
        return Response(serializedData.data)

    def post(self, request):
        questionnaire = questionnaireSerializer(data=request.data)
        if questionnaire.is_valid():
            questionnaire.save()
            return Response(questionnaire.data)
        else:
            return Response(questionnaire.errors)

# class questionnaire(APIView):
#     def get(self, request):
#         id = request.GET.get('id')
        
# @api_view(['GET'])
# def questionnaires(request):
#     questionnaires = questionnaire.objects.all()
#     serializedData = questionnaireSerializer(questionnaires, many=True)
#     return Response(serializedData.data)
    
# @api_view(['GET'])
# def questionnaireById(request):
#     id = request.GET.get('id')
#     print(id)
#     questionnaireSelected = questionnaire.objects.get(id=id)
#     questions = question.objects.get(questionnaire=id)
#     print(questions)
#     serializedData = questionnaireSerializer(questionnaireSelected)
#     return Response(serializedData.data)

# @api_view(['POST'])
# def addQuestionnaire(request):
#     questionnaire = questionnaireSerializer.create()