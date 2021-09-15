from django.db import models
from django.db.models.base import Model
from django.db.models.lookups import UUIDContains
from django.contrib.auth.models import User
from rest_framework import *
import datetime
# Create your models here.


class User_action(models.Model):
    username = models.ForeignKey(User, verbose_name='логин',on_delete=models.CASCADE)
    id = models.BigIntegerField(verbose_name='id',auto_created=True,primary_key=True)
    Credit_card = models.BooleanField(verbose_name='Счет карты кредитный')
    date = models.DateField(verbose_name='Время',default=datetime.datetime.now().strftime('%Y-%m-%d'))
    Amount = models.IntegerField(verbose_name='Сумма')
    currency = models.CharField(verbose_name='Валюта',max_length=10)
    Purpose_of_payment = models.CharField(verbose_name='Назначение платежа',max_length=100)
    MCC_code =  models.IntegerField(verbose_name='МСС код')
    MCC_decode =models.CharField(verbose_name='Расшифровка МСС',max_length=100)
    