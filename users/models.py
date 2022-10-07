from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class RankChoices(models.TextChoices):
        Rookie = ("새내기", "새내기")
        Silver = ("실버", "실버")
        Gold = ("골드", "골드")
        Master = ("마스터", "마스터")

    class PlaceChoices(models.TextChoices):
        JH = ("중화", "중화")
        HP = ("힐스포", "힐스포")
        GH = ("그린힐", "그린힐")
        SK = ("서경스포렉스", "서경스포렉스")
        EM = ("이문", "이문")
        WB = ("웰빙", "웰빙")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    avatar = models.ImageField(
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    rank = models.CharField(
        max_length=10,
        choices=RankChoices.choices,
    )
    place = models.CharField(
        max_length=30,
        choices=PlaceChoices.choices,
    )
    win = models.PositiveIntegerField(
        default=0,
    )
    lose = models.PositiveIntegerField(
        default=0,
    )
    point = models.PositiveIntegerField(
        default=0,
    )
