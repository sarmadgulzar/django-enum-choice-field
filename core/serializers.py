from rest_framework.fields import ChoiceField
from rest_framework.serializers import Serializer

from core.enums import Color


class ColorSerializer(Serializer):
    color = ChoiceField(choices=Color._member_names_)
