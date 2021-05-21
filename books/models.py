from typing import Tuple
from django.db import models

# Create your models here.
# object relation mapping

class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

    

class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    author =models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.id} - {self.title}"

class Review(models.Model):
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now=True)
    Book = models.ForeignKey(Book,on_delete=models.CASCADE, null=True)


