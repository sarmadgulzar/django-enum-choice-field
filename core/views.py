from typing import Optional, Tuple

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import ColorSerializer


class Color2RGBAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ColorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        color = serializer.validated_data["color"]
        return Response({"rgb": self.get_rgb(color)})

    def get_rgb(self, color: str) -> Optional[Tuple[int, int, int]]:
        rgb = None
        match color:
            case "RED":
                rgb = (255, 0, 0)
            case "GREEN":
                rgb = (0, 255, 0)
            case "BLUE":
                rgb = (0, 0, 255)
        return rgb
