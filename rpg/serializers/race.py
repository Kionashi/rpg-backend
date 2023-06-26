from rest_framework import serializers
from ..models.race import Race

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'
