from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages # for showing some info
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'index.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

def registerView(request):
    if request.method == 'POST':

        # collecting user info
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # creating flag for validation
        user_data_has_error = False

        # validating username and email(import User model)
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email is already in use')

        # make sure the password length is at least 5 char long
        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, 'Password must be at least 5 char long')

        # if there is no error create user
        if not user_data_has_error:
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password,
            )

            messages.success(request, 'Account created. Login now')
            return redirect('login')
        else:
            return redirect('register')
    return render(request, 'register.html')

def forgotPassword(request):
    return render(request, 'forgot_password.html')

def passwordResetSent(request):
    return render(request, 'password_reset_sent.html')

def resetPassword(request):
    return render(request, 'reset_password.html')