from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .models import Order
from cart.cart import Cart


class NewOrder(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/new_order.html', {'cart': cart})

    def post(self, request):
        cart = Cart(request)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        address = request.POST.get('address')
        sent_to = email if email else request.user.email
        Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=sent_to,
            city=city,
            address=address
        )
        send_mail(
            'Информация о заказе в книжном магазине Sakura',
            f'{cart.info_for_order()}\n',
            'BookShopSakura@gmail.com',
            [sent_to],
            fail_silently=False,
        )
        cart.clear()
        return redirect('orders:made_order')


class MadeOrder(TemplateView):
    template_name = 'orders/made_order.html'
