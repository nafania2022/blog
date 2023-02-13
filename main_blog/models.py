from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    text = models.TextField()
    now_data = models.DateField(auto_now=True)
    edit_data = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'id_post': self.pk})
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    now_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} {self.email}" 
    
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    