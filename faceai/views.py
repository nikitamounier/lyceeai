from django.http import HttpResponse
from django.shortcuts import render
import os
import requests
from .models import AISession, ResponseImage, RequestImage


imgs = []


def index(request):
    return render(request, 'index.html')


def upload(request):
    url = request.get_raw_uri()
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
        return render(request, 'loading.html', {'description': description})

    # execute if form action is submit_all
    #if request.POST.get('submit_all'):
     #   print("submitted all")
      #  return
        # title = request.POST['title']
        

        # API_KEY = os.getenv('API_KEY')

        # headers = {
        #     'Authorization': f'Bearer {API_KEY}',
        # }

        # files = [
        #     ('tune[callback]', (None, 'https://127:0.0.1:8000/prompt')),
        #     ('tune[title]', (None, title)),
        #     ('tune[branch]', (None, '')),
        #     ('tune[name]', (None, 'person'))
        # ] + [('tune[images][]', open(image, 'rb')) for image in images]

        # response = requests.post('https://api.astria.ai/tunes', headers=headers, files=files)

        # return HttpResponse(response.text)

def prompt(request):
    return HttpResponse('Hello, world...')