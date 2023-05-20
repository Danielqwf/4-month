from django.shortcuts import render
from django.http import HttpResponse
from . import models



def hello_view(request):
    return HttpResponse('Здравствуйте!')


def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'books.html', {'book': book})



