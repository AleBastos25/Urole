from django.contrib import admin

from .models import Role, Comment, List

admin.site.register(Role)
admin.site.register(Comment)
admin.site.register(List)