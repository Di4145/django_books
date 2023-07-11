from django.shortcuts import render
from first.models import Book
# Create your views here.


def list_info(request):
    books = Book.objects.all()
    return render(request, 'info.html', {'books': books})


def book_detail_view(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book.html', {'book': book})

