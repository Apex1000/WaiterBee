from rest_framework import serializers
from orders.models import Order
from social_auth.models import User


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','owner','date')
    