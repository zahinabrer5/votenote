from django.contrib import admin
from .models import *

class PollItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'yes', 'no', 'created_at', 'updated_at')
    ordering = ('-created_at',)

class PollIdAndUserIpAdmin(admin.ModelAdmin):
    list_display = ('ref_id', 'ip')
    ordering = ('-created_at',)

    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

# Register your models here.
admin.site.register(PollItem, PollItemAdmin)
admin.site.register(PollIdAndUserIp, PollIdAndUserIpAdmin)
