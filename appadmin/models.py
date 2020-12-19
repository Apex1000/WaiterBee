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

class FoodDetails(models.Model):
    """ Represents food details """

    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="category_id")
    food_name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Food Details"

class DeliveryPerson(models.Model):
    """ Represents delivery person """

    delivery_person_name = models.CharField(max_length=64)
    delivery_person_phone = models.IntegerField()

    class Meta:
        verbose_name_plural = "Delivery Person"

class Employee:
    """ Restaurant's end operation """

    def add_food_category(self, category_name):
        """ Insert a new food category """

        category_name = FoodCategory(category_name=category_name)
        category_name.save()
        return category_name

    def add_food_details(self, category_id, food_name, price):
        """ Insert new food details """

        food_details = FoodDetails(
            category_id_id=category_id, 
            food_name=food_name, 
            price=price
            )
        food_details.save()
        return food_details

    def add_delivery_person(self, delivery_person_name, delivery_person_phone):
        """ Insert new delivery person """

        details = DeliveryPerson(
            delivery_person_name=delivery_person_name, 
            delivery_person_phone=delivery_person_phone
            )
        details.save()
        return details

    def assign_deliver_person_to_deliver_order(self, order_id, delivery_person_id):
        """ Update CustOrderStatus table to add deliver person to deliver order """

        assign_order = CustOrderStatus.objects\
            .select_related('delivery_person_id')\
            .filter(id=order_id)\
            .update(delivery_person_id_id=delivery_person_id)
        return assign_order

    def view_sales_today(self, order_status):
        """ View revenue/sales of today """
        
        sales_today = cursor.execute("""
            SELECT 
                "fos_custorderstatus"."id", 
                "fos_customerdetails"."cust_name", 
                "fos_custorderstatus"."order_status", 
                "fos_custorderstatus"."bill_amount", 
                "fos_custorderstatus"."checkout_time"
            FROM 
                "fos_custorderstatus" 
            INNER JOIN 
                "fos_customerdetails" 
            ON 
                ("fos_custorderstatus"."cust_id_id" = "fos_customerdetails"."id") 
            WHERE 
                "fos_custorderstatus"."order_status" = {}
            AND
                date("fos_custorderstatus"."checkout_time") = date(CURRENT_DATE)
            """.format(order_status))
        return sales_today

    def sum_revenue_today(self, order_status):
        """ Sum revenue/sales of today """

        revenue_today = cursor.execute("""
            SELECT
                IFNULL(SUM("fos_custorderstatus"."bill_amount"), 0) 
            FROM 
                "fos_custorderstatus" 
            WHERE 
                "fos_custorderstatus"."order_status" = {}
            AND
                date("fos_custorderstatus"."checkout_time") = date(CURRENT_DATE)
            """.format(order_status))
        return revenue_today

    def delete_order(self, order_id):
        """ Delete order """

        del_status =  CustOrderStatus.objects\
            .filter(id=order_id).delete()
        del_selection =  CustOrderSelection.objects\
            .filter(order_id=order_id).delete()
        return del_status, del_selection

class CustOrderStatus(models.Model):
    """ Represents order status """

    cust_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cust_id")
    delivery_person_id = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE, related_name="delivery_person_id", null=True, blank=True)     
    checkout_time = models.DateTimeField(default=timezone.now, blank=True) 
    estimated_time = models.DateTimeField(default=timezone.now, blank=True)
    order_status = models.CharField(max_length=64, null=True, blank=True)
    order_address = models.CharField(max_length=64, null=True, blank=True)
    bill_amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customer Order Status"
