from django.contrib import admin
from djangocustomusersAbstract_app.models import CustomUser

admin.site.register(CustomUser)


class UserAdmin(admin.ModelAdmin):
    list_display = ['status']
