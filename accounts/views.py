from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if(request.method == 'POST'):
        # The user wnats to sign up!
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'password is not match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if(request.method == 'POST'):
        user = auth.authenticate(username =request.POST['username'], password=request.POST['password'])
        if(user is not None):
            auth.login(request, user)
            #obj = Inbox.objects.get()
            return redirect('main_menu')
        else:
            return render(request, 'accounts/login.html', {'error': 'invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'accounts/login.html')