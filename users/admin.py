from django.contrib import admin
from users.models.user_models.user import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "role",
    )
    list_filter = ("role",)
    search_fields = ("fname", "lname", "email")

    def full_name(self, obj):
        return f"{obj.fname} {obj.lname}"

    full_name.short_description = "Full Name"


admin.site.register(User, UserAdmin)
