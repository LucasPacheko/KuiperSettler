from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, 'index.html')