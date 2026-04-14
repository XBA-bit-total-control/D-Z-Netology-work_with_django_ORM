from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = list(Book.objects.all())
    books.sort(key=lambda x: x.pub_date)
    context = {'books': books}

    return render(request, template, context)


def book_view(request, date):
    """
    Может многовато вышло, но что есть
    """
    template = 'books/books_list.html'
    books = Book.objects.all()
    books_pagi = Paginator(books, 1)
    books_pagi_sort = list(books_pagi.object_list)
    books_pagi_sort.sort(key=lambda x: x.pub_date)

    dict_books = {str(v.pub_date): i for i, v in enumerate(books_pagi_sort)}
    dict_books_revers = {i: str(v.pub_date) for i, v in enumerate(books_pagi_sort)}

    page = dict_books[str(date)]

    books = books_pagi_sort[page]

    try:
        ind_b = list(dict_books_revers.keys())[page - 1 if page - 1 > -1 else "m"]
        behind = books_pagi_sort[ind_b].pub_date
    except TypeError:
        behind = 0

    try:
        ind_n = list(dict_books_revers.keys())[page + 1]
        after = books_pagi_sort[ind_n].pub_date
    except IndexError:
        after = 0

    context = {
        'books': [books],
        'behind': behind,
        'after': after
    }

    return render(request, template, context)
