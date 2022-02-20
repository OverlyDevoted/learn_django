from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {'id':5,'title':'john wick'},
        {'id':6,'title':'cars'},
        {'id':7, 'title':'namyuong'}
    ]
}

def learn(request):
    return render(request, 'learn/learn.html', data)

def home(request):
    return HttpResponse("Home page")