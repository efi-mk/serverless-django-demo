from django.contrib import admin

from users.models import Configuration


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    date_hierarchy = "updated"


@admin.register(Configuration)
class UserAdmin(BaseAdmin):
    list_display = ["key", "value"]
    search_fields = ["key"]
