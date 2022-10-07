from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "rank",
                    "username",
                    "password",
                    "name",
                    "email",
                    "win",
                    "lose",
                    "point",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "name",
        "gender",
        "rank",
        "win",
        "lose",
        "point",
    )
