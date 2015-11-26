from django.shortcuts import render

from .models import Book
from .forms import BookAddForm, AuthorAddForm


def main(request):

    books = Book.objects.all()

    form_book = BookAddForm(request.POST or None)
    form_author = AuthorAddForm(request.POST or None)
    # if request.user.is_authenticated():
    #     # books = Book.objects.filter(title=name)
    # else:
    #     books = Book.objects.all()
    #     form = None

    if form_book.is_valid():
        instance = form_book.save(commit=False)
        instance.save()

    if form_author.is_valid():
        instance = form_author.save(commit=False)
        instance.save()

    context = {
        'queryset': books,
        'form_book': form_book,
        'form_author': form_author,
    }
    return render(request, 'main.html', context)
