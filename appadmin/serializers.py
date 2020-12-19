from rest_framework import serializers
from .models import FoodCategory, FoodDetails, DeliveryPerson, CustOrderStatus, CustOrderSelection


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id', 'category_name']

class FoodDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDetails
        fields = ['id', 'category_id','food_name','price']

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = ['id', 'delivery_person_name','delivery_person_phone']

class ViewMenuSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category_id.category_name')
    class Meta:
        model = FoodDetails
        fields = ('id','food_name','price','category')
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustOrderStatus
        fields = ('id','cust_id','delivery_person_id','checkout_time','estimated_time','order_status','order_address','bill_amount')

class OrderSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustOrderSelection
        fields = ('order_id','food_id','food_qty')