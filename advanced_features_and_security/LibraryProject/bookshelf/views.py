from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return HttpResponse("Book List Page")


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return HttpResponse("Book Create Page")


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request):
    return HttpResponse("Book Edit Page")


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request):
    return HttpResponse("Book Delete Page")



def search_books(request):
    query = request.GET.get('q', '')

    books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'books': books})

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
