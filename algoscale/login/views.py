# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.template import RequestContext


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    context = {}
    context.update(csrf(request))
    return render(request, 'login.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    context = {}
    context.update(csrf(request))
    return render(request, 'login.html', context)


def auth_view(request):
    username = request.POST.get('username', "")
    password = request.POST.get('psw', "")
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        print(request.user.username)
        return HttpResponseRedirect('/profile')
    else:
        # args = dict()
        # args["err"] = "Login failed...try registering yourself"
        # args["form"] = RegistrationForm()
        # return render(request, 'register.html', args)
        return HttpResponseRedirect('/user_registration')


@login_required(login_url='/login')
def profile(request):
    login_user_id = request.user.id
    print("login_user_id ::", login_user_id)

    if request.method == "POST":
        try:
            user_id = request.POST.get('user_id', "")
            user_obj = User.objects.get(id=user_id)
            user_obj.delete()
            msg = "Successfully deleted user with ID {0}".format(user_id)
        except:
            if user_id == "":
                msg = "Blank user ID".format(user_id)
            else:
                msg = "Unable to delete user with ID {0}".format(user_id)
        context = {'msg': msg}

    else:
        context = {}

    users = User.objects.all()
    users = users.exclude(id=login_user_id)
    context['users'] = users
    if len(users) == 0:
        context['msg'] = "No user to delete. You are the only user in this system"
    context.update(csrf(request))
    return render(request, 'profile.html', context=context)


def logout(request):
    auth.logout(request)
    msg = "Successfully Logout...."
    return render(request, 'login.html', {"msg": msg})


def user_registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        print("post request")
        form = RegistrationForm(request.POST)
        args["err"] = form.errors
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/register_success')

        args["form"] = form
    else:
        args["form"] = RegistrationForm()
    return render(request, 'register.html', args)


def register_success(request):
    msg = "Register Successful ...Please Login"
    return render(request, 'login.html', {'msg': msg})
