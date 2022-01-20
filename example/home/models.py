from django.db import models
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from datetime import datetime
import random

# Create your models here.


#TODO this is a temp slug creator. If there are better methods please replace.
def create_slug():
    dt = datetime.now()
    random_chars = ""
    for _ in range(0,10):
        random_chars += chr(random.randint(0,25) + ord('a'))

    slug_string = "{}{}{}{}{}{}{}".format("post", dt.month, dt.day, dt.year, dt.second, dt.microsecond, random_chars)
    return slug_string

class Post(models.Model):
    title  = models.CharField(max_length=80)
    body   = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='post_author') 
    public = models.BooleanField(default=True) #TODO should this default to True?

    slug   = models.SlugField(max_length=100, unique=True, default=create_slug)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title + " " + self.body



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')

    #TODO replace name with author and update database
    #author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comment_author') 
    name = models.CharField(max_length=80)

    #email= models.EmailField()
    #title = models.CharField(max_length=80)

    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    #TODO we may want to remove this. I don't understand what this is for. ~Thoth Gunter
    active = models.BooleanField(default=True) 

    class Meta:
        ordering= ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


#TODO this has yet to be connected to the web renderer.
class Image(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    created_on = models.DateTimeField(auto_now_add=True)

    #TODO it is important to sectioning post appropriately, whether through user names or 
    # upload dates.
    image = models.ImageField(upload_to='images') #TODO this may need to be a directory


    def __str__(self):
        return self.title




