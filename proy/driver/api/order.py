from driver.base import BaseView
from driver.serializers import OrderRequestSerializer
from driver.flows.order_flow import OrderFlow

class Order(BaseView):
    request_serializer = OrderRequestSerializer

    def execute_post(self, request, validated_data):
        data, status_code = OrderFlow().order(validated_data)
        return data, status_code
