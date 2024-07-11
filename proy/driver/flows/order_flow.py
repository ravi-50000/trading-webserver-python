import uuid, random
from datetime import datetime
from driver.models import default_database
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from decimal import Decimal
from driver.constants import TOKEN_PRIZE

class OrderFlow:
    def order(self, validated_data):
        try:
            cached_data = cache.get('default_database')
            asset_name = validated_data.get('asset_name')
            order_quantity = Decimal(validated_data.get('order_quantity'))
            exchange_name = validated_data.get('exchange')
            type_of_order = validated_data.get('type_of_order')
            token_prize = TOKEN_PRIZE.get(asset_name)
            order_value = order_quantity * token_prize
            order_id = random.randint(1,1000000)
            current_time = datetime.today()
            if cached_data is None:
                cached_data = default_database
            balance = Decimal(cached_data[exchange_name][asset_name]['Balance'])
            order_cost = token_prize * order_quantity
            if type_of_order == 'BUY':
                if order_value > token_prize:
                    return {'Error': 'Order value exceeds token price'}, status.HTTP_400_BAD_REQUEST
                cached_data[exchange_name][asset_name]['Balance'] += order_value
            else:
                if int(balance)<=0 or order_cost > balance:
                    return {'Error': 'Insufficient balance to SELL order'}, status.HTTP_400_BAD_REQUEST
                cached_data[exchange_name][asset_name]['Balance'] -= order_value
            cached_data[exchange_name][asset_name]['Orders'].append({order_id: {'type_of_order': type_of_order, 'created_at': current_time, 'status': 'ACCEPTED', 'amount': order_value}})
            cache.set('default_database', cached_data, timeout=None)
            return {'Message': f'Order Placed Successfully, Reference_ID = {order_id}'}, status.HTTP_200_OK
        except Exception as e:
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
