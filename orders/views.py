from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request,*args,**kwargs):
    return Response(data="Workers Profile",status=status.HTTP_200_OK)