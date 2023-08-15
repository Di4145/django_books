from django.shortcuts import render
from first.models import Book, Author
from first.models import Janre
# Create your views here.


def search_view(request, id=100):
    q = request.GET.get('author')
    if q:
        books = Book.objects.filter(author__icontains=q)
    else:
        if id == 100:
            books = Book.objects.all()
        else:
            books = Book.objects.filter(janre=id)



    janres = Janre.objects.all()
    authors = Author.objects.all()



    return render(request, 'search.html', {'books': books, 'janres': janres, 'authors': authors})
