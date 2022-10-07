from django.db import models
from common.models import CommonModel


class Notice(CommonModel):
    title = models.CharField(
        max_length=250,
    )
    text = models.TextField()
