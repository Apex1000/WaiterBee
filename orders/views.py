from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrdersSerializer
from .models import Order
from rest_framework import permissions
from .permissions import IsOwner


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrdersSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Order.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
