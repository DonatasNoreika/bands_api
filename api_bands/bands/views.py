from django.shortcuts import render
from rest_framework import generics
from .models import Band
from .serializers import BandSerializer


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
