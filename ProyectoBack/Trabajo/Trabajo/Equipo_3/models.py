from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

class AccessRecord(models.Model):
    webname = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

class Comments(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    text = models.CharField(max_length=100)
