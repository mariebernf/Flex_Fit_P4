from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'cart/cart.html', {'products': products})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if request.method == "POST":
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))

        if not size:
            return redirect('products:product_detail', product_id=product_id)

        product_id = str(product_id)

        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {
                'quantity': quantity,
                'size': size,
            }

        request.session['cart'] = cart

    return redirect('cart:view_cart')


def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart[product_id]['quantity'] = quantity
    else:
        cart.pop(product_id, None)

    request.session['cart'] = cart
    return redirect('cart:view_cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart:view_cart')
