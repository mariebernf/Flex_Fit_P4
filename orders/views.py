from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.context_processors import cart_contents


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('products:product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            cart_data = cart_contents(request)
            order.order_total = cart_data['total']
            order.save()

            request.session['cart'] = {}
            return redirect('checkout_success')

    else:
        form = OrderForm()

    cart_data = cart_contents(request)

    context = {
        'form': form,
        'cart_items': cart_data['cart_items'],
        'total': cart_data['total'],
    }

    return render(request, 'orders/checkout.html', context)

def checkout_success(request):
    return render(request, 'orders/checkout_success.html')
