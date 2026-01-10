from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.context_processors import cart_contents


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('products')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            request.session['cart'] = {}
            return redirect('checkout_success')

    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart_items': cart_contents(request)['cart_items'],
        'total': cart_contents(request)['total'],
    }

    return render(request, 'orders/checkout.html', context)


def checkout_success(request):
    return render(request, 'orders/checkout_success.html')
