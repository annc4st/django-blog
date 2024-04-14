from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list (request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) #it is validating what is received in request.POST against form 
        if form.is_valid():
            #save article to db, associate user with art author 
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article_list')
    else:
        
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})