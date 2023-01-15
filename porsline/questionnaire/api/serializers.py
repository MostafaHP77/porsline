from rest_framework import serializers
from questionnaire.models import questionnaire, question, answer

def name_length(value):
    if len(value) < 3:
        raise serializers.ValidationError("name should not less than 3 charracters")

class answerSerialaizer(serializers.ModelSerializer):
    class Meta():
        model = answer
        fields = "__all__"

class questionSeriallizer(serializers.ModelSerializer):
    # answers = answerSerialaizer(many=True, read_only=True)
    answers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta():
        model = question
        fields = "__all__"

class questionnaireSerializer(serializers.ModelSerializer):
    # description_length = serializers.SerializerMethodField()
    questions = questionSeriallizer(many=True, read_only=True)
    # questions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta():
        model = questionnaire
        fields = "__all__"
        # exclude = ['id']

    # def get_description_length(self, object):
    #     return len(object.description)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('name must be different from description.')
        return data
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("name should not less than 3 charracters")
        return value

# class questionnaireSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return questionnaire.objects.create(**validated_data)

#     def update(self, validated_data, instance):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name must be different from description.')
#         return data