import os

# Create your views here.
from django.shortcuts import render


def get_url(url):
    keys = {}
    with open('local.properties') as f:
        for line in f:
            if '=' in line:
                # Find the name and value by splitting the string
                name, value = line.split('=', 1)
                # Assign key value pair to dict
                # strip() removes white space from the ends of strings
                keys[name.strip()] = value.strip()
                return keys[url]


def index(request):
    music_list = os.listdir(get_url('URL'))
    context = {'list': music_list}
    return render(request, 'one/index.html', context)
