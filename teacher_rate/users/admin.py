from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Image

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    ordering = ('email',)
    list_display = ('email','full_name','date_joined', 'last_login','is_admin','is_staff','is_active','is_superuser')
    search_fields = ('email','full_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Image)