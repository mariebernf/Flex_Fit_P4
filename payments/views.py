import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request):
    order_total = request.session.get('order_total')

    if not order_total:
        messages.error(request, "No order found.")
        return redirect('cart:view_cart')
    
    if request.method == "POST":
        return redirect('checkout_success')


    intent = stripe.PaymentIntent.create(
        amount=int(order_total * 100),  
        currency='eur',
    )

    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, 'payments/payment.html', context)
