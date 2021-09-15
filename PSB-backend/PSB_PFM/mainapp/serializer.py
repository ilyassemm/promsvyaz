from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import User_action
class User_action_serializer(serializers.ModelSerializer):
    class Meta () :
        model = User_action
        fields = ['id','card_number','Credit_card','date','Amount','currency','Purpose_of_payment','MCC_code','MCC_decode']
    def create(self,validated_data):
        return User_action.objects.create(**validated_data)