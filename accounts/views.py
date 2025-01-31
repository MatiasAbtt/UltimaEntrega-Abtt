from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('page-list')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'accounts/login.html')

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada.')
    return redirect('page-list')

# Registro
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Usuario creado con éxito. Ahora puedes iniciar sesión.')
                return redirect('login')
            else:
                messages.error(request, 'El nombre de usuario ya existe.')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')

    return render(request, 'accounts/signup.html')

# Perfil
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Editar perfil (nombre, apellido, email, etc.)
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        request.user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('profile')

    return render(request, 'accounts/edit_profile.html')