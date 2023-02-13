from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *
from .forms import *



def index(request):
    article = Article.objects.all()
    context = {
        'title': 'Главная страница',
        'post': article
               }
    
    return render(request, 'main_blog/index.html', context=context)


def post(request, id_post):
    article = get_object_or_404(Article, pk=id_post)
    context = {
        'title': article.title,
        'post': article
               }
    
    
    return render(request, 'main_blog/post.html', context=context)

def create(request):
    form = UserForm()
    context = {
        'title': "Регистрация",
        'form': form
               }
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():           
            User.objects.create(**form.cleaned_data)
    else:
        form = UserForm()
        return render(request, "main_blog/create.html", context=context)
