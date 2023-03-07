from django.contrib import admin

from onepageapi.stats.models import TgUser, UserForcing


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "tg_id"]


@admin.register(UserForcing)
class UserForcingAdmin(admin.ModelAdmin):
    list_display = ["tg_user", "created_at",]
