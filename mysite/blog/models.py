from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                         .filter(status='published')
class Post(models.Model):
    STATUS_CHOICES=(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )                 
    title= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, null=False)
   
    author= models.CharField(max_length=200, null=True)
    body= models.TextField(max_length=1000)
    date= models.DateTimeField(default=timezone.now)
    status= models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')
    objects= models.Manager()
    published= PublishedManager()
    class Meta:
        ordering=('-date',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.date.year,
                             self.date.month,
                             self.date.day, self.slug])

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    email= models.EmailField()
    body=models.TextField()
    date_added= models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering=('date_added',)
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  