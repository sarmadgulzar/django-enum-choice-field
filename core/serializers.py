from rest_framework.fields import ChoiceField
from rest_framework.serializers import Serializer


class ColorSerializer(Serializer):
    color = ChoiceField(choices=["RED", "GREEN", "BLUE"])