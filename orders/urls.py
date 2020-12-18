from django.urls import path,include
from orders import views
urlpatterns = [
    path('',views.profile),
]
