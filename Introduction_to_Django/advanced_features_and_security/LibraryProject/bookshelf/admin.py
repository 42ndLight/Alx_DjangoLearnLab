from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ("title", "author", "published_date")

    # Enable search functionality on title and author
    search_fields = ("title", "author")

    # Add filtering options for genre and publication date
    list_filter = ("title", "published_date")

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)


# Register the model with the customized admin settings
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)