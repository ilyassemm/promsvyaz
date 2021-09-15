from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import User_action
class User_action_serializer(serializers.ModelSerializer):
    class Meta ():
        model = User_action
        fields = '__all__'