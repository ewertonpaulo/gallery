from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('logout')