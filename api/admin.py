from django.contrib import admin
from .models import Todo, Profile, Contact


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'is_active', 'priority')
	date_hierarchy = "created"
	search_fields = ("title", "description")
	list_editable = ['is_active']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'text')
	search_fields = ('name', 'email', 'text')


admin.site.register(Profile)
