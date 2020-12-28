from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response 

from .models import User
from .serializers import UserSerializer




class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]


class ProfileView(viewsets.ViewSet):
    queryset = User.objects.all()
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
