import uuid, random
from datetime import datetime
from driver.models import default_database
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from decimal import Decimal
from driver.constants import TOKEN_PRIZE

class CancelFlow:
    def cancel(self, validated_data):
        try:
            cached_data = cache.get('default_database') 
            asset_name = validated_data.get('asset_name')
            exchange_name = validated_data.get('exchange')
            order_id = validated_data.get('order_id')
            orders = cached_data[exchange_name][asset_name]['Orders'] #assume some data is present in db
            order_found = False
            order_index = -1
            for index, order in enumerate(orders):
                if order_id in order:
                    order_found = True
                    order_index = index
                    break
            if not order_found:
                return {'Error': f'Reference_ID = {order_id} Does not Exist'}, status.HTTP_400_BAD_REQUEST
            order_creation_time = cached_data[exchange_name][asset_name]['Orders'][order_index][order_id]['created_at']
            current_time = datetime.today()
            time_difference = (current_time-order_creation_time).total_seconds()
            if time_difference > 60:
                return {'Message': f'Sorry your order {order_id} is Executed'}, status.HTTP_400_BAD_REQUEST
            cached_data[exchange_name][asset_name]['Orders'][order_index][order_id].update({'status': 'REJECTED'})
            order_cost = cached_data[exchange_name][asset_name]['Orders'][order_index][order_id]['amount']
            order_type = cached_data[exchange_name][asset_name]['Orders'][order_index][order_id]['type_of_order']
            if order_type == 'BUY':
                cached_data[exchange_name][asset_name]['Balance']-=Decimal(order_cost)
            else:
                cached_data[exchange_name][asset_name]['Balance']+=Decimal(order_cost)
            cache.set('default_database', cached_data, timeout=None)
            return {'Message': 'Order Cancelled Successfully'}, status.HTTP_200_OK
        except Exception as e:
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
