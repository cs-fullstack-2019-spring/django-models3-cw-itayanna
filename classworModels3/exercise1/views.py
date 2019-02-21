from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("Test URL")

#  name, pageNumber, genre, and publishDate attributes

def newBook(request):
    newBook = Book(name="Splintered", pagenumber=653, publishDate="1996-01-01")
    newBook.save()
    return HttpResponse('newBook')
