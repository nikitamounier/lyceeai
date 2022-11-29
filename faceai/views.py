from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import os
import requests
from .models import AISession, ResponseImage, RequestImage
from django.conf import settings

imgs = []


def index(request):
    return render(request, 'index.html')


def upload(request):
    url = request.build_absolute_uri()
    s = url.split("description=")
    if len(s) == 1:
        request.method = "POST"
    else:
        description = url.split("description=")[1].replace("+", " ")
    images = request.FILES.getlist('images')
    for image in images:
        imgs.append(RequestImage.objects.create(image=image))
    if request.method == 'POST':
        return render(request, 'upload.html', {'images': imgs})
    elif request.method == 'GET':
        aiRequest()
        return render(request, 'loading.html', {'description': description})

def aiRequest():
    headers = {
        'Authorization': 'Bearer sd_wyFzfXmVBY9Bo5i7AfGvHjJR6MQgAW',
    }

    files = [
        ('tune[callback]', (None, 'http://127.0.0.1:8000/loading')),
        ('tune[title]', (None, 'my portrait')),
        ('tune[branch]', (None,'')),
        ('tune[name]', (None, 'man')),
    ] + [('tune[images][]', (None, open(settings.MEDIA_ROOT[:-6] + image.image.url, 'rb'))) for image in RequestImage.objects.all()]



    response = requests.post('https://api.astria.ai/tunes', headers=headers, data=files)
    # check if the response was successful
    if response.status_code == 200:
        print(response.status_code, response.json())
    else:
        # if response code is not ok (200), return HTTPResponse with the resulting http error code with description
        print(response.status_code, response.text)
        


def prompt(request):
    return HttpResponse('Hello, world...')