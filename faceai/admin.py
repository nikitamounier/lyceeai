from django.contrib import admin
from .models import AISession, ResponseImage, RequestImage

# Register your models here.

admin.site.register(AISession)
admin.site.register(ResponseImage)
admin.site.register(RequestImage)
