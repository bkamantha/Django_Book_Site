from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='books.all'),
    path('<int:id>',views.show,name='book.show')
]
