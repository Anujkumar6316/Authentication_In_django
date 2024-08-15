from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def loginView(request):
    return render(request, 'login.html')

def registerView(request):
    return render(request, 'register.html')