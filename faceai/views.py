from django.http import HttpResponse
from django.shortcuts import render
import os
import requests

def index(request):
    return render(request, 'faceai/index.html')


def upload(request):
    API_KEY = os.getenv('API_KEY')

    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    files = [
        ('tunecallback', (None, 'https://optional-callback-url.com/to-your-service-when-ready')),
        ('tunetitle', (None, 'my portrait')),
        ('tunebranch', (None, '')),
        ('tune[name]', (None, 'person')),
        ('tune[images][]', open('1.jpg', 'rb')),
        ('tune[images][]', open('2.jpg', 'rb')),
        ('tune[images][]', open('3.jpg', 'rb')),
        ('tune[images][]', open('4.jpg', 'rb')),
    ]

    files += [('tune[images][]', open(f'{i}.jpg', 'rb')) for i in range(5, 11)]

    response = requests.post('https://api.astria.ai/tunes', headers=headers, files=files)
