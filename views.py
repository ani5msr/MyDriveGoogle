from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from django.shortcuts import render, get_object_or_404
from .models import File
from rest_framework import viewsets
from django.contrib.auth.models import User

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer
from rest_framework.authentication import TokenAuthentication
from .decorators import user_check
from django.contrib.auth.decorators import login_required

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = File.objects.all()
@login_required(login_url="/login/")
def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@user_check
@login_required(login_url="/login/")
def file_delete(self, request,):
      user = get_object_or_404(User, id=id)
      if request.method == 'POST':
          user.delete()
          return HttpResponseRedirect(status=status.HTTP_204_NO_CONTENT)
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('fileupload'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
from django.contrib.auth import login as django_login , logout as django_logout
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)