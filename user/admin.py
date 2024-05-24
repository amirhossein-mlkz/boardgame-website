from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import User as bUser


class UserAdmin(BaseUserAdmin):
    list_display = ('firstname', 'lastname', 'phone_number')
    list_display_links = ('firstname', 'lastname')
    readonly_fields = ('last_login', 'joinied_date')
    list_filter = tuple()
    filter_horizontal = tuple()
    ordering = ('-joinied_date',)

    #fields for edit user
    fieldsets = [
        #custom segment name to show in Front: {fields:[list of fields of this segment]}
        (None, {"fields": ["phone_number"]}),
        ("Personal info", {"fields": ["firstname", "lastname"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # fields for add new user
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone_number", "firstname", "lastname", "password1", "password2"],
            },
        ),
    ]    
#admin.site.unregister(bUser)
admin.site.register(User, UserAdmin)
#admin.site.register(User)
