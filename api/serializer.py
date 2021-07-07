from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			"id", "key", "username", "first_name", "last_name", "email", "image",
			"is_active"
		)

	key = serializers.CharField(source="profile.key")
	image = serializers.ImageField(source="profile.image")


class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = (
			"key", "title", "is_active", "is_paused", "is_visible", 'date', 'time'
		)
