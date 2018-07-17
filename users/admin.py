from django.contrib import admin

from users.models import User


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    date_hierarchy = "updated"


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ["user_name", "name"]
    search_fields = ["user_name"]
