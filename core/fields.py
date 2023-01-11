from enum import Enum

from rest_framework.fields import ChoiceField


class EnumChoiceField(ChoiceField):
    error_messages = {
        "invalid_enum_class": "enum must be a subclass of builtin Enum class",
    }

    def __init__(self, enum: Enum, **kwargs):
        if not issubclass(enum, Enum):
            self.fail("invalid_enum_class")
        self.enum = enum
        super().__init__(enum._member_names_, **kwargs)

    def to_internal_value(self, data):
        return self.enum[super().to_internal_value(data)]

    def to_representation(self, value):
        return value.name
