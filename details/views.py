from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework import viewsets

from details.models import *

from details.serializers import *

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):

    queryset= profile.objects.all
    serializer_class = ProfileSerializer
