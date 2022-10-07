from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
