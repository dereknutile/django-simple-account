from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

## app specific
from .models import UserProfile
from .forms import UserForm, UserProfileForm

## set some variables for the scope of this applications views
appName = 'account'
appTitle = appName.title()


def account_login(request):
    template = 'login.html'
    data = {
        'appTitle':appTitle,
        'appUrlBase':'/'+appName+'/',
    }

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            # passed authentication
            if user.is_active:
                
                # is active
                login(request, user)
                return HttpResponseRedirect('/')

            else:
                
                # NOT active, send a message
                return HttpResponse("Your account has disabled.  Contact your administrator.")

        else:
            
            # failed authentication
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # invalid POST
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, template, {})


def account_nda(request):
    template = 'nda.html'
    data = {
        'appTitle':appTitle,
        'appUrlBase':'/'+appName+'/',
    }

    return render(request, template, data)

    
def account_recover(request):
    template = 'recover.html'
    data = {
        'appTitle':appTitle,
        'appUrlBase':'/'+appName+'/',
    }
    
    return render(request, template, data)

    
def account_profile(request):
    template = 'profile.html'
    data = {
        'appTitle':appTitle,
        'appUrlBase':'/'+appName+'/',
    }
    
    return render(request, template, data)


def account_logout(request):
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/account/login/')