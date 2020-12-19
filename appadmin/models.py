from django.db import models, connection 
from social_auth.models import User
from django.utils import timezone

cursor = connection.cursor()

# Create your models here.
class FoodCategory(models.Model):
    """ Represents food categories """

    category_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Food Category"
    
    def __str__(self):
        return self.category_name

class FoodDetails(models.Model):
    """ Represents food details """

    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="category_id")
    food_name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Food Details"
    def __str__(self):
        return self.food_name

class DeliveryPerson(models.Model):
    """ Represents delivery person """

    delivery_person_name = models.CharField(max_length=64)
    delivery_person_phone = models.IntegerField()

    class Meta:
        verbose_name_plural = "Delivery Person"

    def __str__(self):
        return self.delivery_person_name


class CustOrderStatus(models.Model):
    """ Represents order status """

    cust_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cust_id")
    delivery_person_id = models.    ForeignKey(DeliveryPerson, on_delete=models.CASCADE, related_name="delivery_person_id", null=True, blank=True)     
    checkout_time = models.DateTimeField(default=timezone.now, blank=True) 
    estimated_time = models.DateTimeField(default=timezone.now, blank=True)
    order_status = models.CharField(max_length=64, null=True, blank=True)
    order_address = models.CharField(max_length=64, null=True, blank=True)
    bill_amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customer Order Status"

    def __str__(self):
        return self.cust_id

class CustOrderSelection(models.Model):    
    """ Represents food ordered """

    order_id = models.ForeignKey(CustOrderStatus, on_delete=models.CASCADE, related_name="order_id")
    food_id = models.ForeignKey(FoodDetails, on_delete=models.CASCADE, related_name="food_id")  
    food_qty = models.IntegerField()

    class Meta:
        verbose_name_plural = "Customer Order Selection"

