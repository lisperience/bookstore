from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required
def library(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'library.html', context)
