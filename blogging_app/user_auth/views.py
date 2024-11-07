from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .serializers import UserSerializer, LoginSerializer

class LoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        print("request.user ", request.user)
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutAPIView(APIView):
    def post(self, request: Request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
        
    def perform_create(self, serializer: UserSerializer):
        try:
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)