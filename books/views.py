from django.shortcuts import render
from django.http import HttpResponse
import json



# Create your views here.
bookdata  =  open('books.json').read()

data = json.loads(bookdata)

def index(request):
    context = {'books':data}
    return render(request, 'books/index.html', context)


def show(request,id):
    singlebook =list()
    for book in data:
        if book['id'] == id:
            singlebook = book

    context = {'book':singlebook}
    return render(request, 'books/show.html', context)