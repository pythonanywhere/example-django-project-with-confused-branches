# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def home(request):
    return render(request, 'home.html', {'posts': list(BlogPost.objects.all())})

