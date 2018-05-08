import os

from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.template import loader

from muzlo.settings import URL


def index(request):
    musicList = os.listdir(URL)
    context = {'list': musicList}
    return render(request, 'one/index.html', context)
