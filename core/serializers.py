from rest_framework.serializers import Serializer

from core.enums import Color
from core.fields import EnumChoiceField  # new line


class ColorSerializer(Serializer):
    color = EnumChoiceField(enum=Color)  # updated line
