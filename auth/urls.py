from django.urls import path
from auth.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, UpdateUserImageView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('dashboard/update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('dashboard/change_image/<int:pk>/', UpdateUserImageView.as_view(), name='auth_image'),
    path('dashboard/logout/', LogoutView.as_view(), name='auth_logout'),
]
