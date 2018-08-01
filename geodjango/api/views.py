from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Laptop, MenbersPoint
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializer import UserSerializer, GroupSerializer,  CordenateMenbersSerializer, LoginSerializer, CordenateLaptopSerializer
from  django.contrib.auth import (login as django_login ,logout as django_logout)
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
 
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CordenatesMembersViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CordenateMenbersSerializer
    queryset = MenbersPoint.objects.all()
 
class CordenatesLaptopViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
   
    serializer_class = CordenateLaptopSerializer
    queryset = Laptop.objects.all()


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user = user)
        return Response({"token": token.key}, status = 200 )

class LogoutinView(APIView):
      authentication_classes = (TokenAuthentication, )
      def post(self,request):
           django_logout(request)
           return Response(status= 204,)
           
    