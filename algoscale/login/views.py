# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
        msg = "Wrong Username or Password ....Please Try again."
        return render(request, 'login.html', {'msg': msg})


@login_required(login_url='/')
def profile(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    context.update(csrf(request))
    return render(request, 'profile.html', context=context)


def delete_user(request):
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

    return render(request, 'profile.html', {'msg': msg})
