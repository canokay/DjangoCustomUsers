from django.contrib import admin
from djangocustomusersAbstract_app.models import User

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ['status']
