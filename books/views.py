from typing import List
from django.db import models
from django.db.models.base import Model
from books.models import Book, Review
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView


# This is using generic view
class Booklistview(ListView):
    #context_object_name = "books"
    def get_queryset(self):
        return Book.objects.all()

# This is without using generic view

# def index(request):
#     dbData = Book.objects.all()
#     context = {'books': dbData}
#     return render(request, 'books/index.html', context)


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-time_stamp')
        context['authors'] = context['book'].author.all()
        return context

# def show(request, id):
#     singlebook = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-time_stamp')
#     context = {'book': singlebook, 'reviews': reviews}
#     return render(request, 'books/show.html', context)


def review(request, id):
    review = request.POST['review']
    reviewdb = Review(body=review, book_id=id)
    reviewdb.save()
    return redirect('/books')
