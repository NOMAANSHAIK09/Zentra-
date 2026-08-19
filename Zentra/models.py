from django.db import models

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()


    def __str__(self):
        return self.name
