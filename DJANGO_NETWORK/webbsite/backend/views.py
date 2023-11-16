from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from .serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer



# class UserLoginView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']
#         user = authenticate(request, username=email, password=password)
#
#         if user is not None:
#             login(request, user)
#             return Response({
#                 "user": UserLoginSerializer(user, context=self.get_serializer_context()).data,
#                 "message": "User logged in successfully"
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response({
                "user_id": user.id,
                "email": user.email,
                "message": "User logged in successfully"
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)

# class UserLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data.get('email', '')
#         password = request.data.get('password', '')

#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             return Response({
#                 "user_id": user.id,
#                 "email": user.email,
#                 "message": "User logged in successfully"
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
class ImageV(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageP(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
