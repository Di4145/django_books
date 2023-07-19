from django.shortcuts import render
from first.models import Book, Author
from first.models import Janre
# Create your views here.


def search_view(request, id=100):
    janres = Janre.objects.all()
    authors = Author.objects.all()


    if id == 100:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(janre=id)
    return render(request, 'search.html', {'books': books, 'janres': janres, 'authors': authors})