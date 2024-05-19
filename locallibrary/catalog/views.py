from django.shortcuts import render
from .models import Book, BookInstance, Genre, Author
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all().count()

    return render(request, 'index.html', context={
        'num_books':num_books, 'num_instances':num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors, 'num_genres': num_genres
    })

class BookListView(generic.ListView):
    model = Book
    paginate_by = 1


class BookDetailView(generic.DetailView):
    model = Book