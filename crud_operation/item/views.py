from django.shortcuts import render
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer

# Create your views here.

class ItemView(APIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
