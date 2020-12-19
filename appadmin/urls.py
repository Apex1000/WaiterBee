from django.urls import path,include
from appadmin import views

urlpatterns = [
    path('employees/add-food-category',views.FoodCategoryListAPIView.as_view(),name='appadmin'),
    path('employees/category/<int:id>', views.FoodCategoryDetailAPIView.as_view(), name="appadmin"),
    path('employees/add-food-details',views.FoodDetailsListAPIView.as_view(),name='appadmin'),
    path('employees/food/<int:id>', views.FoodDetailsAPIView.as_view(), name="appadmin"),
    path('employees/add-delivery-person', views.DeliveryPersonListAPIView.as_view(), name="appadmin"),
    path('menu/', views.ViewMenuListAPIView.as_view(), name="appadmin"),
    path('create-order/', views.OrderListAPIView.as_view(), name="appadmin"),
    path('add-food-to-order/', views.OrderSelectionListAPIView.as_view(), name="appadmin"),
    path('cart/<int:order_id>/', views.DeleteOrderSelectionListAPIView.as_view(), name="appadmin"),
    path('checkout/<int:order_id>/', views.CheckOut.as_view(), name="appadmin"),
]
