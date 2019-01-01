import os

from django.conf import settings
from django.db import models

from django.contrib.auth import get_user_model



class Players(models.Model):
    address = models.CharField(max_length=128, default="")
    session_key = models.CharField(max_length=128)

class Bets(models.Model):
    status = models.BooleanField(default=0)
    player = models.CharField(max_length=128)
    win_number = models.IntegerField(default=0)
    numbers = models.CharField(max_length=128, default="")
    amount = models.FloatField(default=0)
    win_amount = models.FloatField(default=0)
    tx_hash = models.CharField(max_length=128)
    oracle_query_id = models.CharField(max_length=128, default="")
    contract = models.CharField(max_length=128)
    blocknumber = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
