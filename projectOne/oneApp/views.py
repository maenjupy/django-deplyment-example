from django.shortcuts import render
from .forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'oneApp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'oneApp/index.html', {})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'oneApp/index.html', {'user':user, 'username':username})

            else:
                return render(request, 'oneApp/index.html', {})
        else:
            values = True
            return render(request, 'oneApp/user_login.html', {'values':values})

    else:
        return render(request, 'oneApp/user_login.html', {})

def user_register(request):

    errorit = False
    register = False

    if request.method == 'POST':
        user_form = ProfileForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            username = request.POST.get('username')
            register = True

        else:
            errorit = True

    else:
        user_form = ProfileForm()


    return render(request, 'oneApp/user_register.html', {'register':register, 'user_form': user_form, 'errorit': errorit})
