from rest_framework import serializers
from .models import Match


class MatchSerializer(serializers.Serializer):
    pk = serializers.IntegerField(
        read_only=True,
    )
    test_player = serializers.CharField(
        required=True,
    )
    test_opposite = serializers.CharField(
        required=True,
    )
    player_point = serializers.IntegerField(
        required=True,
    )
    opposite_point = serializers.IntegerField(
        required=True,
    )
    place = serializers.ChoiceField(
        choices=Match.PlaceChoices.choices,
    )

    def create(self, validated_data):
        return Match.objects.create(**validated_data)
