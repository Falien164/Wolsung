from .models import Character
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['first_name', 'last_name', 'age']
