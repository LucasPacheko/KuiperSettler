from django.shortcuts import render
from .models import User


# Create your views here.
def register(request):
    return render(request, 'register.html')


def users(request):
    new_user = User()
    new_user.email = request.POST.get('email')
    new_user.password = request.POST.get('password')
    new_user.save()

    users = {'users': User.objects.all()}

    return render(request, 'user_list.html', users)
