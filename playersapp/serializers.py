from django.http import QueryDict
from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('id',)

    def to_internal_value(self, data):
        # Convert empty strings to None (NULL)

        # Convert QueryDict to a mutable dictionary, because "data[field] = None" raises AttributeError: This QueryDict instance is immutable
        data_mutable = QueryDict(mutable=True)
        for field, value in data.items():
            if value == '':
                data_mutable[field] = None
            else:
                data_mutable[field] = value
        return super().to_internal_value(data_mutable)
