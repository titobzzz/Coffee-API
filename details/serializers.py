from rest_framework import serializers
from details.models import *




class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = profile
        fields="__all__"