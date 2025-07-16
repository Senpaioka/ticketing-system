from django.contrib import admin
from account.models import UserAccount

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):

    list_display = ['username', 'email', 'is_staff']
    list_display_links = ['email']
    list_editable = ['is_staff']
    readonly_fields = ['password']


admin.site.register(UserAccount, UserAccountAdmin)