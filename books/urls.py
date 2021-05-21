from . import views
from django.urls import path


urlpatterns = [
    path('',views.Booklistview.as_view(),name='books.all'),
    path('<int:pk>',views.BookDetailView.as_view(),name='book.show'),
    path('<int:id>/review',views.review,name="book.review")
]
