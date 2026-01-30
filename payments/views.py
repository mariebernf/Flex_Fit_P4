import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from orders.models import Order


stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request):
    order_number = request.session.get("order_number")
    if not order_number:
        messages.error(request, "No order found.")
        return redirect("cart:view_cart")


    order = get_object_or_404(Order, order_number=order_number)

    if request.method == "POST":
        return redirect("checkout_success", order_number=order.order_number)

    intent = stripe.PaymentIntent.create(
        amount=int(order.order_total * 100),
        currency='eur',
    )


    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }


    return render(request, "payments/payment.html", {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
        "order_number": order_number,
    })
