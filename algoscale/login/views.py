# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')
    context = {}
    context.update(csrf(request))
    return render(request, 'login.html', context)

