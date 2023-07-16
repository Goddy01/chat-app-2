from django.contrib import admin
from .models import UserProfile
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ['user', 'full_name', 'email', 'bio']

admin.site.register(UserProfile, UserProfileAdmin)