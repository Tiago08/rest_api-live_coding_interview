from rest_framework import serializers
from .models import ShowData

class ShowDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowData
        fields = ('id', 'name', 'address')