from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    Register View for creating a new user with optional fields.

    The view is inherited from CreateAPIView.

    - Username and password are required.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    """
    Login View for obtaining a new access and refresh token pair.

    The view is inherited from TokenObtainPairView. The view is used to obtain a new access and refresh
    token pair by providing a valid username and password.

    The view is extended to return user data in the response.
    """

    # return user data in response
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data["username"])
        serializer = UserSerializer(user)
        response.data["user"] = serializer.data
        return response
