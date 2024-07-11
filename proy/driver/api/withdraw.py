from driver.base import BaseView
from driver.serializers import WithdrawRequestSerializer
from driver.flows.withdraw_flow import WithdrawFlow

class Withdraw(BaseView):
    request_serializer = WithdrawRequestSerializer

    def execute_post(self, request, validated_data):
        data, status_code = WithdrawFlow().withdraw(validated_data)
        return data, status_code
