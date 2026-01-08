from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'cart/cart.html', {'products': products})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    cart[str(product_id)] = cart.get(str(product_id), 1)
    request.session['cart'] = cart

    return redirect('cart:view_cart')
