from bookstore import books
from django.db.models.base import Model
from books.models import Book
from django.shortcuts import redirect, render ,get_object_or_404
from django.http import HttpResponse
from django.http import Http404



def index(request):
    dbData = Book.objects.all()
    context = {'books':dbData}
    return render(request, 'books/index.html', context)



def show(request,id):
    singlebook = get_object_or_404(Book,pk=id)
    context = {'book':singlebook}
    return render(request, 'books/show.html', context)


def review(request):
    return redirect('/books')
