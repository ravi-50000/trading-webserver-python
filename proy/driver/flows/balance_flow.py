import uuid, random
from datetime import datetime
from driver.models import default_database
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from decimal import Decimal
from driver.constants import TOKEN_PRIZE

class BalanceFlow:
    def balance(self, validated_data):
        try:
            cached_data = cache.get('default_database')
            asset_list = validated_data.get('asset_name', [])
            exchange_list = validated_data.get('exchange', [])
            if cached_data is None:
                cached_data = default_database
            results = {}
            if not exchange_list and not asset_list:
                for exchange, assets in cached_data.items():
                    results[exchange] = {}
                    for asset, data in assets.items():
                        results[exchange][asset] = data['Balance']
            elif exchange_list and asset_list:
                for exchange in exchange_list:
                    if exchange in cached_data:
                        results[exchange] = {}
                        for asset in asset_list:
                            if asset in cached_data[exchange]:
                                results[exchange][asset] = cached_data[exchange][asset]['Balance']
            elif exchange_list:
                for exchange in exchange_list:
                    if exchange in cached_data:
                        results[exchange] = {}
                        for asset, data in cached_data[exchange].items():
                            results[exchange][asset] = data['Balance']
            elif asset_list:
                for exchange, assets in cached_data.items():
                    results[exchange] = {}
                    for asset in asset_list:
                        if asset in assets:
                            results[exchange][asset] = assets[asset]['Balance']

            return {'Balance(s)': results}, status.HTTP_200_OK
        except Exception as e:
            return {'error': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
