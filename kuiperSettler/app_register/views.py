from django.shortcuts import render
# from .models import User
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    return render(request, 'register.html')


def users(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.create_user(username, password=password)
    user.save()


    users = {'users': User.objects.all()}

    return render(request, 'user_list.html', users)
