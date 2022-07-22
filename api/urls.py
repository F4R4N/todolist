from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserView)

urlpatterns = [
	path('todo/', views.TodoGetView.as_view()),
	path('todo/add/', views.TodoCreateView.as_view()),
	path("todo/edit/<key>", views.TodoUpdateView.as_view()),
	path("todo/delete/<key>", views.TodoDelView.as_view()),
	path("user/", include(router.urls)),
	path('contact/', views.ContactView.as_view()),
]
