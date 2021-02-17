from django.contrib import admin
from .models import Todo, Profile

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'is_active', 'priority')
	date_hierarchy = "created"
	search_fields = ("title", "description")
	list_editable = ['is_active']

admin.site.register(Profile)

