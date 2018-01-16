__author__ = 'ryan'
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render_to_response('base.html')


#Login Page
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login1.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')
