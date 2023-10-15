from django.urls import path
from .views import CaServiceView, ServiceListView, ServiceCreateView

urlpatterns = [
    path('create', ServiceCreateView.as_view()),
    path('', ServiceListView.as_view()),
    path('<ca_id>', CaServiceView.as_view()),
]