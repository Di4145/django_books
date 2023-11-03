import requests
from django.shortcuts import render
from first.models import Book, USD


# Create your views here.


def list_info(request):
    books = Book.objects.all()


    usd = USD.objects.last()
    rate_usr_rub = usd.usd_now
    return render(request, 'info.html', {'books': books, 'rate_usr_rub': rate_usr_rub})


def book_detail_view(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book.html', {'book': book})

