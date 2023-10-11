from rest_framework import serializers
from .models import CaService


class CaServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaService
        fields = '__all__'
        lookup_field = 'ca_id'
