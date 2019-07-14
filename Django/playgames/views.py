from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from playgames.models import Stones
from playgames.serializers import StoneSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.generic import TemplateView

from .models import Stones

class PlayPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class userAPI(generics.ListCreateAPIView):
    queryset = Stones.objects.all()
    serializer_class = StoneSerializer

class getStones(generics.ListCreateAPIView):
    queryset = Stones.objects.all()
    serializer_class = StoneSerializer
