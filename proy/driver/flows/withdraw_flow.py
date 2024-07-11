import uuid, random
from datetime import datetime
from driver.models import default_database
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from decimal import Decimal

class WithdrawFlow:
    def withdraw(self, validated_data):
        try:
            print(validated_data)
            cached_data = cache.get('default_database')
            exchange_name = validated_data.get('exchange')
            amount = Decimal(validated_data.get('amount'))
            address = validated_data.get('address')
            asset_name = validated_data.get('asset_name')
            print(amount)
            if cached_data is None:
                cached_data = default_database
            balance = cached_data[exchange_name][asset_name]['Balance']
            print(balance)
            if amount > balance:
                return {'Error': 'Insufficient funds to Withdraw'}, status.HTTP_400_BAD_REQUEST
            cached_data[exchange_name][asset_name]['Balance']-=amount 
            cache.set('default_database', cached_data, timeout=None)
            return {'Message': 'Withdraw Successfully Done'}, status.HTTP_200_OK

        except Exception as e:
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
