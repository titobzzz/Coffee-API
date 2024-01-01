from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework import viewsets

from details.models import *

from details.serializers import *

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):

    queryset= profile.objects.all
    serializer_class = ProfileSerializer


    def perform_create(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid(raise_exception= True):
            serializer.save()
            response_data= {
                "data":serializer.data,
                "message":"Data created successfully"
            }
            return Response(response_data)
       

        