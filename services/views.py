from django.shortcuts import render
from .models import CaService
from .serializers import CaServiceListSerializer
from rest_framework.generics import RetrieveAPIView


class CaServiceView(RetrieveAPIView):
    queryset = CaService.objects.all()
    serializer_class = CaServiceListSerializer
    lookup_field = 'ca_id'
