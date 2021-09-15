from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .serializer import User_action
from .models import User
from .serializer import User_action_serializer
import pandas
from rest_framework.response import Response
from .models import User_action
# Create your views here.
@api_view(['GET'])
def chisto_pod_exsel(request):
    data = pandas.read_excel('1.xlsx')
    data_list =data.values.tolist()
    
    for item in data_list:
        
        try:
            user= User.objects.create_user(str(item[0]),'test','1234')
            user.save()
        except:
            print('БЛЯЯЯ '+ str(item))
        # bool_inmodel = True
        # if item[2] =='Нет': 
        #     bool_inmodel = False если понадобиться использовать булевку, а не да\нет

        dic = {
            'id':str(item[0]),
            'card_number':item[1],
            "Credit_card":item[2],
            "date":item[3], 
            "Amount":item[4], 
            "currency":item[5], 
            "Purpose_of_payment":item[6], 
            "MCC_code":item[7], 
            "MCC_decode":item[8]

        }
        serializer = User_action_serializer(data=dic)

        if serializer.is_valid():
            print(item)
            serializer.save()
        else :
            print(serializer.errors)
            return Response()

        
