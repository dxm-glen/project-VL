from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    # 데이터베이스에 적용되지 않고 재사용을 위해서만 사용되는 모델임을 표시
    class Meta:
        abstract = True
