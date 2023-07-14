from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from . import models
# Register your models here.

class MessagesAdmin(ImportExportModelAdmin):
    list_display = ['user', 'sender', 'recipient', 'date', 'is_read']
    list_filter = ['is_read']

admin.site.register(models.Message, MessagesAdmin)