from django.db import models
from decimal import Decimal

# Create your models here.
default_database = {
    'a': {
        'BITCOIN':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
        'ETHEREUM':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
    },
    'b': {
        'BITCOIN':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
        'ETHEREUM':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
    },
    'c': {
        'BITCOIN':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
        'ETHEREUM':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
    },
    'd': {
        'BITCOIN':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
        'ETHEREUM':{
            'Balance': Decimal('0.00'),
            'Orders': [],
        },
    },
}
