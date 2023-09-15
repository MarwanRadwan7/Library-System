from django.urls import path
from django.contrib.auth.decorators import  login_required
from django.conf.urls.static import static
from django.conf import settings
from .views import all_books, borrow, show_details, user_borrowed_books, available_books, return_back

app_name = "books"
urlpatterns = [
    path('all', all_books, name='books.index'),
    path('my-books',user_borrowed_books , name='books.borrowedBooks'),
    path('available',available_books , name='books.available'),
    path("<int:id>", show_details, name="books.show"),
    path('borrow/<int:id>',borrow , name='books.borrow'),
    path("return/<int:id>", return_back, name="books.return")
    
] 