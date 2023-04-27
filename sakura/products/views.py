from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
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
        context = {
            'book': book,
            'reviews': reviews,
            'form': form
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




