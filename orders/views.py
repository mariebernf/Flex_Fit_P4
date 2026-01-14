from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.context_processors import cart_contents
from .models import OrderLineItem


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('products:product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the order
            order = form.save(commit=False)
            cart_data = cart_contents(request)
            order.order_total = cart_data['total']
            order.save()

            # Create order line items
            for item in cart_data['cart_items']:
                OrderLineItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    size=item['size'],
                )

            # Clear the cart
            request.session['cart'] = {}

            # Redirect to success page
            return redirect('checkout_success', order_number=order.order_number)
    else:
        form = OrderForm()

    # Always get cart data to display in template
    cart_data = cart_contents(request)

    context = {
        'form': form,
        'cart_items': cart_data['cart_items'],
        'total': cart_data['total'],
    }

    return render(request, 'orders/checkout.html', context)


def checkout_success(request, order_number):
    return render(request, 'orders/checkout_success.html', {
        'order_number': order_number
    })
