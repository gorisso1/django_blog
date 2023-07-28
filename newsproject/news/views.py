
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .form import ArticleForm
def news_list(request):
    news_items = News.objects.all()
    return render(request, 'news/news_list.html', {'news_items': news_items,'user': request.user})
# Create your views here.
def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("hello")
            return redirect('login')
        else:
            print(form.errors)

    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    return render(request, 'news/login.html', {'form': form})





def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = ArticleForm()

    return render(request, 'news/create_article.html', {'form': form})
