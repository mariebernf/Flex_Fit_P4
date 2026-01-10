from django.shortcuts import render
from cart.context_processors import cart_contents


def checkout(request):
    cart = cart_contents(request)

    context = {
        'cart_items': cart['cart_items'],
        'total': cart['total'],
    }

    return render(request, 'orders/checkout.html', context)
