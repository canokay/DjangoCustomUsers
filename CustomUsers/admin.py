from django.contrib import admin
from CustomUsers.models import Profile, UserStatus

# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "userStatus"]

    class Meta:
        model = Profile


@admin.register(UserStatus)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["userStatus"]

    class Meta:
        model = UserStatus
