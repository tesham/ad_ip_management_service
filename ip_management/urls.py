
from django.urls import path
from .views import *

urlpatterns = [
    path('ip', IPAPIView.as_view(), name='ip_api_view'),
]