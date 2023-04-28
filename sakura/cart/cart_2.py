"""def add(self, product):
    product_id = str(product.id)
    if product_id not in self.cart:
        self.cart[product_id] = {'quantity': 1, 'price': str(product.price * )}
    else:
        self.cart[product_id]['quantity'] += 1
    self.save()"""

"""def __iter__(self):
    books_ids = self.session['cart'].keys()
    books = Book.objects.filter(id__in=books_ids)
    for book in books:
        self.cart[str(book.id)]['book'] = book

    for item in self.session['cart'].values():
        item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item"""