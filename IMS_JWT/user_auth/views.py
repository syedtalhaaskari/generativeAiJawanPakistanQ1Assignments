from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

# from .permissions import IsModeratorOrSuperUser
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser, IsAuthenticatedOrReadOnly])
def create_or_get_users(request: Request):
    if request.method == 'GET':
        data = User.objects.all()
        users = []
        for user in data:
            users.append({
                "email": user.email,
                "username": user.username,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser
            })
        return Response(users, status=status.HTTP_200_OK)
    if request.method == 'POST':
        try:
            data = request.data

            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])

                User.objects.create(**serializer.validated_data)

                serializer.validated_data.pop('password')
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh_token = RefreshToken.for_user(user)

        response_data = {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }
        response = Response()
        response.data = response_data
        response.status = status.HTTP_201_CREATED
        response.set_cookie(
            key='refresh',
            value=response_data['refresh'],
            secure=True,
            httponly=True,
        )
        response.set_cookie(
            key='access',
            value=response_data['access'],
            secure=True,
            httponly=True,
        )

        return response
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def logout_view(request):
    refresh_token = request.data.get('refresh')

    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)