from django.urls import path, include
from . import views

from rest_framework import permissions, routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

router = routers.DefaultRouter()
router.register('user', views.UserView)

schema_view = get_schema_view(
	openapi.Info(
		title="Snippets API",
		default_version='v1',
		description="all you need to know about the shop api is in the following documentation please dont bother.",
		contact=openapi.Contact(email="farantgh@gmail.com"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	path('todo/', views.TodoGetView.as_view()),
	path('todo/add/', views.TodoCreateView.as_view()),
	path("todo/edit/<key>", views.TodoUpdateView.as_view()),
	path("todo/delete/<key>", views.TodoDelView.as_view()),
	path("user/", include(router.urls)),
	path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui')

]