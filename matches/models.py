from django.db import models
from common.models import CommonModel

# Create your models here.


class Match(CommonModel):
    class PlaceChoices(models.TextChoices):
        중화 = ("중화", "중화")
        힐스포 = ("힐스포", "힐스포")
        그린힐 = ("그린힐", "그린힐")
        서경대 = ("서경스포렉스", "서경스포렉스")
        이문 = ("이문", "이문")
        웰빙 = ("웰빙", "웰빙")

    test_player = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    test_opposite = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    player = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="players",
        null=True,
        blank=True,
    )

    opposite = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="opposites",
        null=True,
        blank=True,
    )
    player_point = models.PositiveIntegerField()
    opposite_point = models.PositiveIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    place = models.CharField(
        max_length=20,
        choices=PlaceChoices.choices,
    )

    def playername(self):
        return self.player.name

    def oppositename(self):
        return self.opposite.name
