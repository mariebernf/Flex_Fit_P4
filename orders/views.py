from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.context_processors import cart_contents
from .models import Order, OrderLineItem
from django.contrib.auth.decorators import login_required


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('products:product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()

            cart_data = cart_contents(request)
            order.order_total = cart_data['total']
            order.save()

            for item in cart_data['cart_items']:
                OrderLineItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    size=item['size'],
                )

            request.session["order_number"] = order.order_number
            return redirect("payments:payment")

    else:
        form = OrderForm()

    cart_data = cart_contents(request)

    context = {
        'form': form,
        'cart_items': cart_data['cart_items'],
        'total': cart_data['total'],
    }

    return render(request, 'orders/checkout.html', context)


def checkout_success(request, order_number):
    # Clear the cart/session
    request.session['cart'] = {}
    request.session.pop("order_total", None)
    request.session.pop("order_number", None)

    return render(request, 'orders/checkout_success.html', {
        'order_number': order_number
    })


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'orders/order_history.html', {'orders': orders})
