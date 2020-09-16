# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib import auth


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
