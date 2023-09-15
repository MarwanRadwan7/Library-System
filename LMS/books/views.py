from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from datetime import date, timedelta
from books.models import Book
from status.models import Status

def lms_index(request):
    return render(request, 'index.html')


def all_books(request):
    available= Status.objects.get(name='Available')
    available_books = Book.objects.filter(status= available)
    borrowed= Status.objects.get(name='Borrowed')
    borrowed_books = Book.objects.filter(status= borrowed)
    return render( request, "all-books.html", context={'available_books': available_books, 'borrowed_books': borrowed_books} )

def available_books(request):
    available= Status.objects.get(name='Available')
    books = Book.objects.filter(status= available)
    return render(request, 'available-books.html', context={'books': books})


# def borrowed_books(request):
#     borrowed= Status.objects.get(name='Borrowed')
#     borrowed_books = Book.objects.filter(status= borrowed)
#     pass


def show_details(request, id):
    book = Book.get_book(id=id)
    print(book.status_id)
    return render( request, "book-details.html", context={'book': book})


def borrow(request, id):
    book = Book.get_book(id=id)
    if request.method == "POST":
            status = Status.objects.get(name='Borrowed')
            book.status = status
            book.user = request.user
            borrow_period = int(request.POST['borrow_period'])
            borrow_date = date.today()
            return_date = borrow_date + timedelta(days=borrow_period)

            book.borrow_period = borrow_period
            book.borrow_date = borrow_date
            book.return_date = return_date
            book.save()
            return redirect('books:books.borrowedBooks')
    return render(request , "book-borrow.html", context={'book': book})
            


def user_borrowed_books(request):
    books = Book.objects.filter(user=request.user)
    print(request.user)
    return render(request , "my-borrowed-books.html", context={"books":books})


def return_back(request, id):
    book = Book.get_book(id=id)
    available = Status.objects.get(name='Available') 
    book.status = available
    book.borrow_date = None
    book.borrow_period = None
    book.return_date =None
    book.user = None
    book.save()
    return redirect('books:books.borrowedBooks')