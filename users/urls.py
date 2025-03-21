from django.urls import path
from users.views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path(
        "token_refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Refresh token endpoint
]
