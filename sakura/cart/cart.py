from decimal import Decimal
from products.models import Book

CART_SESSION = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION)
        if not cart:
            cart = self.session[CART_SESSION] = {}
        self.cart = cart

    def save(self):
        self.session[CART_SESSION] = self.cart

    def clear(self):
        self.session[CART_SESSION] = {}

    def add(self, book):
        book_id = str(book.id)
        if book_id not in self.cart.keys():
            self.cart[book_id] = {'amount': 1, 'price': str(book.price)}
        else:
            self.cart[book_id]['amount'] += 1
        self.save()

    def __iter__(self):
        books_ids = self.session['cart'].keys()
        books = Book.objects.filter(id__in=books_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.session['cart'].values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['amount']
            yield item

    def remove(self, book):
        book_id = str(book.id)
        if self.cart[book_id]['amount'] > 1:
            self.cart[book_id]['amount'] -= 1
            self.save()
        else:
            del self.cart[book_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['amount'] for item in self.cart.values())

    def get_total_amount(self):
        return sum(item['amount'] for item in self.cart.values())








