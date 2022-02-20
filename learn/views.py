from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

data = {
    'movies': [
        {'id':5,'title':'john wick'},
        {'id':6,'title':'cars'},
        {'id':7, 'title':'namyuong'}
    ]
}

def learn(request):
    data = Movie.objects.all()
    echo: data
    return render(request, 'learn/learn.html', {'movies': data})

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'learn/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/learn')

    return render(request, 'learn/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/learn')