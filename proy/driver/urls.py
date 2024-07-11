from django.urls import path
from driver.api.order import Order
from driver.api.cancel import Cancel
from driver.api.balance import Balance
from driver.api.withdraw import Withdraw
from django.http import HttpResponse

def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path('order/', Order.as_view(), name='order'),
    path('cancel/', Cancel.as_view(), name='cancel'),
    path('balance/', Balance.as_view(), name='balance'),
    path('withdraw/', Withdraw.as_view(), name='withdraw'),
    path('health/', health, name='health'),
]
