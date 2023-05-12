from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Article

from django.shortcuts import render, redirect
from .forms import ArticleForm
# Create your views here.

# def home(request):
    
#     return HttpResponse("hello ")

def home(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'article.html', {'form': form})




def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})

def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('home')