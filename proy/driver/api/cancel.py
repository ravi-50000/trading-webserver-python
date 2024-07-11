from driver.base import BaseView
from driver.serializers import CancelRequestSerializer
from driver.flows.cancel_flow import CancelFlow

class Cancel(BaseView):
    request_serializer = CancelRequestSerializer

    def execute_post(self, request, validated_data):
        data, status_code = CancelFlow().cancel(validated_data)
        return data, status_code
