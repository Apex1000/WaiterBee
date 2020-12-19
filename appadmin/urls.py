from django.urls import path,include
from appadmin import views

urlpatterns = [
    path('employees/add-food-category',views.FoodCategoryListAPIView.as_view(),name='appadmin'),
    path('employees/category/<int:id>', views.FoodCategoryDetailAPIView.as_view(), name="appadmin"),
    path('employees/add-food-details',views.FoodDetailsListAPIView.as_view(),name='appadmin'),
    path('employees/food/<int:id>', views.FoodDetailsAPIView.as_view(), name="appadmin"),
    path('employees/add-delivery-person', views.DeliveryPersonListAPIView.as_view(), name="appadmin"),
    path('menu/', views.ViewMenuListAPIView.as_view(), name="appadmin"),
    path('addorder/', views.OrderListAPIView.as_view(), name="appadmin"),
]
