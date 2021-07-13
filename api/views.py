from rest_framework import permissions, status, generics, viewsets
from rest_framework.response import Response
from .models import Todo, Contact
from rest_framework.views import APIView
from .serializer import TodoSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAdminUser, )


class ContactView(APIView):
	permission_classes = (permissions.AllowAny, )

	def post(self, request, format=None):
		contact = Contact.objects.create(
			name=request.data['name'],
			email=request.data['email'],
			text=request.data['text']
		)
		contact.save()
		return Response(status=status.HTTP_201_CREATED, data={'detail': "created"})


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
		empty_fields = {}
		message = "field value not provided"
		keys = ['title', 'is_active', 'is_paused', 'is_visible', 'date', 'time']
		for key in keys:
			if key not in request.data:
				empty_fields[key] = message
		if len(empty_fields) != 0:
			return Response(status=status.HTTP_400_BAD_REQUEST, data=empty_fields)
		todo = Todo.objects.create(
			title=request.data["title"],
			user=user,
			is_active=request.data['is_active'],
			is_paused=request.data['is_paused'],
			is_visible=request.data['is_visible'],
			date=request.data['date'],
			time=request.data['time']
		)
		todo.save()
		return Response(data={"detail": "created"}, status=status.HTTP_200_OK)


class TodoUpdateView(APIView):
	permission_classes = (permissions.IsAuthenticated, )

	def put(self, request, key, format=None):
		user = request.user
		todo = get_object_or_404(Todo, key=key, user=user)
		if 'title' in request.data:
			todo.title = request.data['title']
		elif 'is_active' in request.data:
			todo.is_active = request.data['is_active']
		elif 'is_paused' in request.data:
			todo.is_paused = request.data['is_paused']
		elif 'is_visible' in request.data:
			todo.is_visible = request.data['is_visible']
		elif 'date' in request.data:
			todo.date = request.data['date']
		elif 'time' in request.data:
			todo.time = request.data['time']
		else:
			return Response(
				data={"detail": "all fields was empty"},
				status=status.HTTP_400_BAD_REQUEST
			)

		todo.save()
		return Response(data={"detail": "updated"}, status=status.HTTP_200_OK)


class TodoDelView(APIView):
	permission_classes = (permissions.IsAuthenticated, )

	def delete(self, request, key, format=None):
		user = request.user
		todo = get_object_or_404(Todo, key=key, user=user)
		todo.delete()
		return Response(data={"detail": "deleted"}, status=status.HTTP_200_OK)
