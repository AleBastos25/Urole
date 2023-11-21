from django.contrib import admin

from .models import Role, Comment

admin.site.register(Role)
admin.site.register(Comment)