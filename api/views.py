from rest_framework import permissions, status, generics
from rest_framework.response import Response
from .models import Todo, Profile
from rest_framework.views import APIView
from .serializer import TodoSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class TodoGetView(generics.ListAPIView):
	serializer_class = TodoSerializer
	permission_classes = (permissions.IsAuthenticated, )
	
	def get_queryset(self):
		user = self.request.user
		return Todo.objects.filter(user=user)


class TodoCreateView(APIView):
	permission_classes = (permissions.IsAuthenticated, )
	
	def post(self, request, format=None):
		user = request.user
		user_todos = Todo.objects.filter(user=user)
		for user_todo in user_todos:
			if request.data['title'] in user_todo.title:
				return Response(status=status.HTTP_409_CONFLICT)
		todo = Todo.objects.create(
			title=request.data["title"],
			user=user,
			)
		if 'description' in request.data:
			todo.description = request.data['description']
		if 'image' in request.data:
			todo.image = request.data['image']
		if 'is_active' in request.data:
			todo.is_active = request.data['is_active']
		if 'priority' in request.data:
			todo.priority = request.data['priority']
		if 'send_email' in request.data:
			todo.send_email = request.data['send_email']
		todo.save()
		return Response(data={"detail": "created"}, status=status.HTTP_200_OK)


class TodoUpdateView(APIView):
	permission_classes = (permissions.IsAuthenticated, )

	def put(self, request, key, format=None):
		user = request.user
		user_todos = Todo.objects.filter(user=user)
		todo = get_object_or_404(Todo, key=key)
		if 'title' in request.data:
			for user_todo in user_todos:
				if request.data['title'] in user_todo.title and request.data['title'] != todo.title:
					return Response(status=status.HTTP_409_CONFLICT)
			todo.title = request.data['title']
		if 'description' in request.data:
			todo.description = request.data['description']
		if 'image' in request.data:
			todo.image = request.data['image']
		if 'is_active' in request.data:
			todo.is_active = request.data['is_active']
		if 'priority' in request.data:
			todo.priority = request.data['priority']
		if 'send_email' in request.data:
			todo.send_email = request.data['send_email']
		todo.save()
		return Response(data={"detail": "updated"}, status=status.HTTP_200_OK)

class TodoDelView(APIView):
	permission_classes = (permissions.IsAuthenticated, )

	def delete(self, request, key, format=None):
		user = request.user
		user_todos = Todo.objects.filter(user=user)
		todo = get_object_or_404(Todo, key=key)
		todo.delete()
		return Response(data={"detail": "deleted"}, status=status.HTTP_200_OK)