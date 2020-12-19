from django.contrib import admin
from appadmin.models import FoodCategory,FoodDetails,DeliveryPerson,CustOrderStatus,CustOrderSelection
# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(FoodDetails)
admin.site.register(DeliveryPerson)
admin.site.register(CustOrderStatus)
admin.site.register(CustOrderSelection)