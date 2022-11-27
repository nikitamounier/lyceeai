from django.db import models

class AISession(models.Model):
    prompt = models.TextField()
    timestamp = models.DateTimeField('date created')

    def __str__(self):
        return f"{self.prompt, self.timestamp}"

class ResponseImage(models.Model):
    image = models.ImageField(upload_to='images/')
    session = models.ForeignKey(AISession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image, self.session}"

class RequestImage(models.Model):
    image = models.ImageField(upload_to='images/')
    #session = models.ForeignKey(AISession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image, self.session}"