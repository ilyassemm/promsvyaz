from django.db import models
from django.db.models.base import Model
from django.db.models.lookups import UUIDContains
from django.contrib.auth.models import User,AbstractUser
from rest_framework import *
import datetime
from django.conf import settings
# Create your models here.

class User_action(models.Model):
    action_id = models.AutoField(verbose_name='id',auto_created=True,primary_key=True)
    id = models.ForeignKey(User,on_delete=models.CASCADE)
    card_number = models.IntegerField(verbose_name='Сумма')
    Credit_card = models.CharField(verbose_name='Счет карты кредитный',max_length=4)
    date = models.CharField(verbose_name='Время',max_length=10)
    Amount = models.FloatField(verbose_name='Сумма')
    currency = models.CharField(verbose_name='Валюта',max_length=11)
    Purpose_of_payment = models.CharField(verbose_name='Назначение платежа',max_length=100)
    MCC_code =  models.FloatField(verbose_name='МСС код',null=True)
    MCC_decode =models.CharField(verbose_name='Расшифровка МСС',max_length=100,null=True)
    