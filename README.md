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

### **3. Working on Register View:**
- Change static file links in all files.```<link rel="stylesheet" href="{% static 'style.css' %}">```
- Head to register.html and give input fields a name attribute and csrf_token and change the login url:
```html
<form method="POST">
        {% csrf_token %}
        <div class="txt_field">
            <input type="text" required name="first_name">
            <span></span>
            <label>First Name</label>
          </div>

          <div class="txt_field">
            <input type="text" required name="last_name">
            <span></span>
            <label>Last Name</label>
          </div>

        <div class="txt_field">
          <input type="text" required name="username">
          <span></span>
          <label>Username</label>
        </div>

        <div class="txt_field">
            <input type="email" required name="email">
            <span></span>
            <label>Email</label>
          </div>

        <div class="txt_field">
          <input type="password" required name="password">
          <span></span>
          <label>Password</label>
        </div>    

        <!-- <div class="pass">Forgot Password?</div> -->
        <input type="submit" value="Register">
        <div class="signup_link">
          Already have an account? <a href="login.html">Login</a>
        </div>
      </form>
```

**NOTE:**<HR>
- name attributes in the html acts as the unique identifier for us to work with the data.
<hr>

- In registerView view check for incoming form submission and grab user data.
```py
if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
```
- validate the data provided

    - create flag for error```user_data_has_error = False```
    - validate email and username
    ```py
    # validating username and email(import User model)
    if User.objects.filter(username=username).exists():
        user_data_has_error = True
        messages.error(request, 'Username already exists')

    if User.objects.filter(email=email).exists():
        user_data_has_error = True
        messages.error(request, 'Email is already in use')
    ```
    - validate password length
    ```py
    # make sure the password length is at least 5 char long
    if len(password) < 5:
        user_data_has_error = True
        messages.error(request, 'Password must be at least 5 char long')
    ```

- create a new user if there are no errors and redirect them to the login page. else back to the register page with errors.
```py
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
```

- Display incoming messages in ```register.html```, ```login.html```, ```forgot_password.html``` and ```reset_password.html``` files.
```html
{% if messages %}
    {% for message in messages %}
        {% if message.tags == 'error' %}
            <center><h4 style="color: firebrick;">{{message}}</h4></center>
        {% else %}
            <center><h4 style="color: dodgerblue;">{{message}}</h4></center>
        {% endif %}
    {% endfor %}
{% endif %}

<form method="POST">
```
- Test the code to check if users can now register.

### **4. Login User Feature**
