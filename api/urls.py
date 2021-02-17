from django.urls import path, include
from . import views

urlpatterns = [
	path('todo/', views.TodoGetView.as_view()),
	path('todo/add/', views.TodoCreateView.as_view()),
	path("todo/edit/<key>", views.TodoUpdateView.as_view()),
	path("todo/delete/<key>", views.TodoDelView.as_view()),


]