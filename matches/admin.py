from django.contrib import admin
from .models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):

    list_display = (
        "test_player",
        "player_point",
        "test_opposite",
        "opposite_point",
        "place",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "place",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
