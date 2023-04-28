from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import messages
from .models import Book, Review
from django.views import View
from .forms import ReviewForm


class Index(View):
    def get(self, request):
        books = Book.objects.filter(available=True)
        return render(request, 'products/index.html', {'books': books})


class BookDetail(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        reviews = book.reviews.all()
        form = ReviewForm()
        if len(reviews) != 0:
            total_rating = sum(map(lambda x: x.score, reviews))
            average_rating = round(total_rating / len(reviews), 1)
            quantity_of_reviews = len(reviews)
        else:
            average_rating = 0
            quantity_of_reviews = 0
        context = {
            'book': book,
            'reviews': reviews,
            'form': form,
            'average_rating': average_rating,
            'quantity_of_reviews': quantity_of_reviews

        }
        return render(request, 'products/book_detail.html', context)


class AddReview(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = ReviewForm(request.POST)
        if not Review.objects.filter(author=request.user, book=book).exists():
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.book = book
                review.save()
                return redirect('products:book_detail', book_id=book_id)
        else:
            messages.success(request, 'Один отзыв - одна книга.')
            return redirect('products:book_detail', book_id=book_id)


class DeleteReview(View):
    def post(self, request, review_id):
        print(request.method)
        review = get_object_or_404(Review, id=review_id)
        if review.author == request.user:
            review.delete()
            return redirect('products:book_detail', review.book.id)
        else:
            raise PermissionDenied()


class AuthorOfBooks(View):
    def get(self, request, author):
        books = Book.objects.filter(author=author)
        return render(request, 'products/author_of_books.html', {'books': books, 'author': author})


class Search(View):
    def get(self, request):
        search_query = request.GET.get('search')
        if search_query:
            books = Book.objects.filter(
                Q(author__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(genre__name__icontains=search_query)
            )
        else:
            books = Book.objects.all()

        if books.count() == '0':
            title = 'Соответствий не найдено'
        else:
            title = 'Все то, что удалось найти'

        context = {
            'title': title,
            'books': books
        }
        return render(request, 'products/search.html', context)
