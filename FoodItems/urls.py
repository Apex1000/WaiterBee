from django.urls import path,include
from FoodItems import views
urlpatterns = [
    path('',views.item_list),
]
