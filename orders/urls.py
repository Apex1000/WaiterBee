from django.urls import path,include
from orders import views
urlpatterns = [
    path('',views.ExpenseListAPIView.as_view(),name='orders'),
    path('',views.ExpenseDetailAPIView.as_view(),name='orders'),
]
