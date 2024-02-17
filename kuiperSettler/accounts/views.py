from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_handle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')


def logout_handle(request):
    logout(request)
    return redirect('/')
