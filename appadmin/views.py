from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import FoodCategorySerializer, FoodDetailsSerializer, DeliveryPersonSerializer, ViewMenuSerializer, OrderSerializer,OrderSelectionSerializer
from .models import FoodCategory, FoodDetails, DeliveryPerson, CustOrderStatus, CustOrderSelection
from rest_framework import permissions

# Create your views here.

class FoodCategoryListAPIView(ListCreateAPIView):
    serializer_class = FoodCategorySerializer
    queryset = FoodCategory.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class FoodCategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FoodCategorySerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = FoodCategory.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter()

class FoodDetailsListAPIView(ListCreateAPIView):
    serializer_class = FoodDetailsSerializer
    queryset = FoodDetails.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class FoodDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FoodDetailsSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = FoodDetails.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter()

class DeliveryPersonListAPIView(ListCreateAPIView):
    serializer_class = DeliveryPersonSerializer
    queryset = DeliveryPerson.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

class ViewMenuListAPIView(ListAPIView):
    serializer_class = ViewMenuSerializer
    queryset = FoodDetails.objects.select_related('category_id').all()
    # permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter()

class OrderListAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = CustOrderStatus.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(cust_id=1)

class OrderSelectionListAPIView(ListCreateAPIView):
    serializer_class = OrderSelectionSerializer
    queryset = CustOrderSelection.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter()

class DeleteOrderSelectionListAPIView(DestroyAPIView,UpdateAPIView):
    serializer_class = OrderSelectionSerializer
    queryset = CustOrderSelection.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "order_id"
    def get_queryset(self):
        return self.queryset.filter()

class CheckOut(UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = CustOrderStatus.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter()