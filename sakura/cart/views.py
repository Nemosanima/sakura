from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from products.models import Book


def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def add_to_cart(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.add(book)
    return redirect('cart:cart')


def remove_from_cart(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart')


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart')




