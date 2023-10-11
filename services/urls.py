from django.urls import path
from .views import CaServiceView

urlpatterns = [
    path('<ca_id>', CaServiceView.as_view()),
]