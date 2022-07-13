import email
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    number = models.IntegerField()
    bio = models.TextField()
    mail = models.EmailField()



    def __str__(self):
        return self.user.username


class subCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    subcategory = models.ForeignKey(subCategory, on_delete=CASCADE)

    def __str__(self):
        return self.title


class filmType(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Script(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    subcategory = models.CharField(max_length=250)
    filmtype = models.CharField(max_length=250)
    seller = models.CharField(max_length=250)
    synopsis = models.TextField()
    logline = models.TextField()
    treatment = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    firstpage = models.FileField(upload_to='media')
    pageCount = models.IntegerField()
    discount_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Professional(models.Model):
    country = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=100)
    talent = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    bio = models.TextField()
    rate = models.IntegerField()
    image = models.ImageField(upload_to="media/professional_images")
    joined_on = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name

class Talent(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class About(models.Model):
    about = models.TextField()
    offer = models.TextField()
    vision = models.TextField()
    
    def __str__(self):
        return self.about


class Term(models.Model):
    copyright = models.TextField()
    
    def __str__(self):
        return self.copyright


class LikePost(models.Model):
    script_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Hiring(models.Model):
    hirername = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    professional = models.CharField(max_length=100)



    def __str__(self):
        return self.hirername



class Blog(models.Model):
    headline = models.CharField(max_length=100)
    story = models.TextField()
    image = models.ImageField(upload_to="media/news_images")
    date_posted = models.DateTimeField(default=datetime.now)
    posted_by = models.CharField(max_length=100)

    def __str__(self):
        return self.headline

