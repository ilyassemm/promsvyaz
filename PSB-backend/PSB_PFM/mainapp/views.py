from django.db.models import fields
from django.shortcuts import render
from django.core import serializers
# from rest_framework import serializers
from rest_framework.decorators import api_view
from .serializer import User_action
from .models import User
from .serializer import User_action_serializer
import pandas as pd
import json
from rest_framework.response import Response 
from .models import User_action
# Create your views here.
@api_view(['POST'])
def add_transac_info(request):
        
    transac_info =  json.loads(request.body())

        
    serializer = User_action_serializer(data=dic)

    if serializer.is_valid():

        serializer.save()
    else :
        print(serializer.errors)
        return Response()

@api_view(['GET'])
def test (request,id):
    user = serializers.serialize("json", 
            User_action.objects.all().filter(id=str(id)))   #вызываем все 
                                                            #все строки из бд
                                                            # с этим значением
    json_user = json.loads(user)
    #через цикл делаем датафрейм 
    # чтобы быстрее прогонять и искать
    # нужный ответ
    all_transactions = pd.DataFrame()
    for dictionary in json_user:
        for key, value in dictionary.items():

            if key == 'fields':
                df = pd.json_normalize(value)
                all_transactions = all_transactions.append(df)

    chars = {
    'ID': 0,
    'Rich': False,

    'Major': False,
    'Traveller': False,
    'Hamster': False,
    'Wide': False,

    'Poor': False,
    'Burn': False,
    'Migrant': False,

    'Fitmost': False,
    'Flowers': False,
    'Coffee': False
    }
    try:
        chars['ID'] = int(id)

        user_transactions = all_transactions.loc[
            all_transactions['id'] == int(id)]  # все транзакции пользователя

        user_expenses = user_transactions.loc[user_transactions['Amount'] < 0]  # все траты пользователя
        total_expenses = -user_expenses['Amount'].sum()

        user_refill = user_transactions.loc[user_transactions['Amount'] > 0]
        total_refill = user_refill['Amount'].sum()

        # MCC codes starts
        user_transfers = user_transactions.loc[(user_transactions['MCC_code'] == 4829) & (user_transactions['Amount'] < 0)]  # все перевводы пользователя
        total_transfers = -user_transfers['Amount'].sum()
        # print(total_transfers)

        user_travellings = user_transactions.loc[(user_transactions['MCC_code'] == 4304) 
            & (user_transactions['MCC_code'] == 4415) & (user_transactions['MCC_code'] == 4418) 
            & (user_transactions['MCC_code'] == 4511) & (user_transactions['MCC_code'] == 4582) 
            & (user_transactions['MCC_code'] == 5309) & (user_transactions['MCC_code'] == 5947) 
            & (user_transactions['MCC_code'] == 7011) & (user_transactions['MCC_code'] == 4011)
            & (user_transactions['MCC_code'] == 4112) & (user_transactions['MCC_code'] == 3113) 
            & (user_transactions['Amount'] < 0)]
        total_travellings = -user_travellings['Amount'].sum()

        user_fitmost = user_transactions.loc[(user_transactions['MCC_code'] == 5655) 
            & (user_transactions['MCC_code'] == 5940) & (user_transactions['MCC_code'] == 5941) 
            & (user_transactions['Amount'] < 0)]  # все перевводы пользователя
        total_fitmost = -user_fitmost['Amount'].sum()

        user_flowers = user_transactions.loc[(user_transactions['MCC_code'] == 5193) 
            & (user_transactions['MCC_code'] == 5992) & (user_transactions['Amount'] < 0)]  # все перевводы пользователя
        total_flowers = -user_flowers['Amount'].sum()

        user_coffee = user_transactions.loc[(user_transactions['MCC_code'] == 5462) 
            & (user_transactions['Amount'] < 0)]  # все перевводы пользователя
        total_coffee = -user_coffee['Amount'].sum()
        # MCC codes ends

        if total_refill - total_expenses >= 0:  # проверка на положительный баланс
            chars['Rich'] = True

        if total_refill - total_expenses < 0:  # проверка на отрицательный баланс
            chars['Poor'] = True


        if total_expenses >= 115000:  # проверка на мажора
            chars['Major'] = True


        if total_refill / total_expenses >= 2:
            chars['Hamster'] = True

        if total_refill / total_expenses >= 1 and total_refill / total_expenses < 2:
            chars['Wide'] = True

        if total_refill / total_expenses >= 0 and total_refill / total_expenses < 0.5:
            chars['Burn'] = True

        if total_transfers / total_expenses >= 1:
            chars['Migrant'] = True

        if total_travellings / total_expenses >= 0.3:
            chars['Traveller'] = True

        if total_fitmost >= 5000:
            chars['Fitmost'] = True
        if total_flowers >= 2000:
            chars['Flowers'] = True
        if total_coffee >= 500:
            chars['Coffee'] = True
        # print(chars)
        chars_= {k: v for k, v in chars.items() if v!=False}
        # print(chars_)
    except:
        return Response(data={},status=200)
    
    return Response(data=chars_,status=200)
        
