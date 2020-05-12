from django.db import models

# Create your models here.
class Client(models.Model):
    # create table t1(name text)
    name = models.CharField(max_length=264)

    # create table t1(email text)
    email = models.EmailField(unique=True)

    # create table t1(email text)
    url = models.URLField()

    def __str__(self):
        return self.name



    

