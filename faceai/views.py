from django.http import HttpResponse
from django.shortcuts import render
import os
import requests
from .models import AISession, ResponseImage, RequestImage

def index(request):
    return render(request, 'faceai/index.html')


def upload(request):
    images = request.FILES.getlist('images')
    for image in images:
        RequestImage.objects.create(image=image)
    images = RequestImage.objects.all()
    if request.method == 'POST':
        return render(request, 'faceai/upload.html', {'images': images})
    elif request.method == 'GET':
        return HttpResponse('Hello, world. You\'re at the upload website now.')

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
    return HttpResponse('Hello, world. You\'re at the prompt website now.')