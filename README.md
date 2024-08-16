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
- Again add name attribute, csrf_token and add register url
- add static file 
- In ```loginView``` view check for incoming form submission and grab user data
```py
if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
```

- Authenticate the user details
```py
user = authenticate(request=request, username=username, password=password)
if user is not None:
    login(request, user)
    return redirect('home')
else:
    messages.error(request, 'Invalid username or password')
    return redirect('login')
```

- Restrict access to home page to authenticated users
```py
@login_required
def home(request):
    pass
```

- Set ```LOGIN_URL``` in ```settings.py``` file.
```py
# where authenticated user gets redirected to when they try to access a loing required view.
LOGIN_URL = 'login'
```
**NOTE**<HR>
This LOGIN_URL redirect the user, where login is required to the login page
<hr>

- Test if user can login.

### **5. Logout Users Feature**
- create logout view.
```py
def logoutView(request):
    logout(request)
    return redirect('login')
```
- Create logout url.```path('logout/', views.logoutView, name='logout'), ```
- Test the code.

### **6. Forgot Password Model & Views**
- Create the views for ```forgotPassword```, ```passwordResetSent```, and ```resetPassword```.
```py
def forgotPassword(request):
    return render(request, 'forgot_password.html')

def passwordResetSent(request, reset_id):
    return render(request, 'password_reset_sent.html')

def resetPassword(request, reset_id):
    return render(request, 'reset_password.html')
```

- Again add static files, csrf_token, url.
- Add urls path for the given views.
```py
path('forget-password/', views.forgotPassword, name='forget_password'),
path('password-reset-sent/<str:reset_id>/', views.passwordResetSent, name='password_reset_sent'),
path('reset-password/<str:reset_id>/', views.resetPassword, name='reset_password'),
```
- Create the model for the password reset.
```py
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class passwordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Password reset for {self.user.username} at {self.created_at}'
```

- Make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

- add this model to admin 
```py 
from django.contrib import admin
from .models import passwordReset

# Register your models here.
admin.site.register(passwordReset)
```

### **7. Forgot Password Feature**
- Again repeat the process add name attribute, csrf_token and change url.
- And in the ```forgotPassword``` view collect the user data.
```py
if request.method == "POST":
    email = request.POST.get('email')
```
- Check if email is already exists or not.
- if email exist the send the email to registed email id with the reset url.
```py
def forgotPassword(request):
    if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            new_reset_password = passwordReset(user=user)
            new_reset_password.save()

            password_reset_url = reverse('reset_password', kwargs={'reset_id': new_reset_password.reset_id})

            # email content
            email_body = f'Reset your password using the link below:\n\n\n{password_reset_url}'

            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body, # email body
                settings.EMAIL_HOST_USER, #sender
                [email] # reciever
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('password_reset_sent', reset_id = new_reset_password.reset_id)
        
        except User.DoesNotExist:
            messages.error(request, f'No user with email "{email}" found.')
            return redirect('forgot_password')
         
    return render(request, 'forgot_password.html')
```
- else show the error message.
- Setup email settings so we can send password reset email in ```settings.py```.
```py
# setup email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'anujkumar63166316@gmail.com'
EMAIL_HOST_PASSWORD = 'grzn tgge ejnc vvte'
```

### **8. Password Reset Sent View:**
- Get reset_id and make sure that it is valid
```py
def passwordResetSent(request, reset_id):
    if passwordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        # redirect to forgot password page if code does not exists
        messages.error(request, 'Invalid reset id')
        return redirect('forgot_password')
```

### **9. Password Reset View:**
- Head to the ```reset_password.html``` file and make sure that we add the name attributes and csrf_token.
- Get the reset_id and make sure that it is valid.
- Get the password from form submit.
```py
if request.method == 'POST':
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
```
- varify passwords and reset link.
```py
passwords_have_error = False

if password1 != password2:
    passwords_have_error=True
    messages.error(request, 'Passwords does not match')
        
if len(password1) < 5:
    passwords_have_error=True
    messages.error(request, 'Password must be atleast 5 char long')

# check if link is not expired
expiration_time = reset_id.created_at + timezone.timedelta(minutes=10)
    
if timezone.now()>expiration_time:
    passwords_have_error=True
    messages.error(request, 'Reset link has expired')
```