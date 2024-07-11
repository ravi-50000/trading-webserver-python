from driver.base import BaseView
from driver.serializers import BalanceRequestSerializer
from driver.flows.balance_flow import BalanceFlow

class Balance(BaseView):
    request_serializer = BalanceRequestSerializer

    def execute_post(self, request, validated_data):
        data, status_code = BalanceFlow().balance(validated_data)
        return data, status_code
