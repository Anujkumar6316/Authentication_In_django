# Authentication_In_django<br>

## **AIM:**
- Login
- Logout
- Register
- Reset password

## **Steps to complete this project:**
<br>

### **1. Setting up a django project:**
- create virtual environment.
- Install django in venv.
- create django project(AuthenticationProject)
- create Core app.
- create templates folder(same as manange.py loc).
- add templates in dirs in settings.py file.
- register the app in the settings.py file.
- create urls for the app and register them in the project's urls.
- setup static files in settings.py
```py
import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
```

**NOTE**
<HR>
<div style='background-color:gray;'>

- STATIC_URL sets the URL prefix for serving static files.
- STATIC_ROOT sets the physical directory where Django collects and serves static files from.
- STATICFILES_DIRS sets the directories where Django looks for static files in your project.

</div>
<HR>
 
- Create template files. eg: index.html, login.html, register.html, forgot_password.html, password_reset_sent.html, reset_password.html
- Make required imports.
- Make migrations
- create a superuser.

### **2. Creating home, register & login views:**
- view.py(Core)
```py
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def loginView(request):
    return render(request, 'login.html')

def registerView(request):
    return render(request, 'register.html')
```

- create url for each view: urls.py(Core)
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
]
```