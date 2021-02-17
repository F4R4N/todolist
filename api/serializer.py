from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("id", "username", "first_name", "last_name", "email", "image")
	image = serializers.ImageField(source="profile.image")

class TodoSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Todo
		fields = ("key", "title", "description", "image", "user", "is_active", "priority", "send_email")

