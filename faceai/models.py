from django.db import models

class Session(models.Model):
    prompt = models.CharField(max_length=500)
    timestamp = models.DateTimeField('date created')

class Image(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')