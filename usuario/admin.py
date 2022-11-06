from django.contrib import admin

from usuario.models import Autor, Orientador, Usuario
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.register(Autor)
admin.site.register(Orientador)


@admin.register(Usuario)
class myUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("id", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("id",)
