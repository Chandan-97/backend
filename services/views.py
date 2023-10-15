from django.shortcuts import render
from .models import CaService
from .serializers import CaServiceListSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class CaServiceView(RetrieveAPIView):
    queryset = CaService.objects.all()
    serializer_class = CaServiceListSerializer
    lookup_field = 'ca_id'


class ServiceListView(ListAPIView):
    queryset = CaService.objects.all()
    serializer_class = CaServiceListSerializer


class ServiceCreateView(APIView):

    def post(self, request, format=None):
        data = self.request.data
        try:
            service = data.dict()
            CaService.objects.create(**service)
            return Response({"Message": "Saved successfully"})
        except Exception as e:
            print(e)
            return Response({"Message": e.__str__()}, status=400)
