from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField
import datetime



class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    post_image = models.ImageField(null=True, blank=True,upload_to='images/')
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='sport')

    def __str__(self):
        return f'{str(self.title)}   |  {str(self.author)}'

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

    def latest_posts(self):
        reference = datetime.date.today() - datetime.timedelta(days=7)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        return tomorrow > self.post_date > reference
