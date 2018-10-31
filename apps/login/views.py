from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from apps.login.forms import LoginForm
# Create your views here.


def login_user(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return logout_user(request)
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    if form.is_valid():
                        login(request, user)
                        return redirect('index')
                    else:
                        print(form.errors)
                        messages.error(request, 'No es posible ingresar')
                else:
                    messages.error(request, 'Usuario Inactivo en el Sistema')
            else:
                try:
                    if User.objects.get(username=username) is not None:
                        messages.error(request,'No se puede ingresar al sistema. Consulte al administrador')
                        return redirect('login')
                except User.DoesNotExist:
                    messages.error(request, 'Usuario Inválido')
                    return redirect('login')

        contexto = {'form': form}
        return render(request, 'login/login.html', contexto)

def logout_user(request):
    logout(request)
    return redirect('login')