from rest_framework import serializers
from driver.constants import WHITELISTED_ADDRESS_SET, EXCHANGE, ASSETS, ORDER

class OrderRequestSerializer(serializers.Serializer):
    exchange = serializers.ChoiceField(choices=EXCHANGE)
    asset_name = serializers.ChoiceField(choices=ASSETS)
    order_quantity = serializers.DecimalField(max_digits=8, decimal_places=2)
    type_of_order =  serializers.ChoiceField(choices=ORDER)

class CancelRequestSerializer(serializers.Serializer):
    exchange = serializers.ChoiceField(choices=EXCHANGE)
    asset_name = serializers.ChoiceField(choices=ASSETS)
    order_id = serializers.IntegerField()
    
class BalanceRequestSerializer(serializers.Serializer):
    exchange = serializers.ListField(child=serializers.ChoiceField(choices=EXCHANGE), required=False)
    asset_name = serializers.ListField(child=serializers.ChoiceField(choices=ASSETS), required=False)

class WithdrawRequestSerializer(serializers.Serializer):
    exchange = serializers.ChoiceField(choices=EXCHANGE)
    asset_name = serializers.ChoiceField(choices=ASSETS)
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    address = serializers.ChoiceField(choices=WHITELISTED_ADDRESS_SET)
