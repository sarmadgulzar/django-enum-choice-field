from django.urls import path

from core.views import Color2RGBAPIView

urlpatterns = [
    path("color2rgb", Color2RGBAPIView.as_view(), name="color2rgb"),
]
