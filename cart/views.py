from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    order_total = 0

    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, id=item_id)

        if isinstance(item_data, int):
            quantity = item_data
            size = None
        else:
            quantity = int(item_data.get('quantity', 0))
            size = item_data.get('size')

        if quantity <= 0:
            continue

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'size': size,
        })

        order_total += product.price * quantity

    request.session['order_total'] = float(order_total)

    context = {
        'cart_items': cart_items,
        'order_total': order_total,
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if request.method == "POST":
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))

        
        if not size:
            return redirect('products:product_detail', product_id=product_id)

        
        if product_id in cart:
            existing = cart[product_id]
            if isinstance(existing, int):
                cart[product_id] = existing + quantity
            else:
                existing_qty = int(existing.get('quantity', 0))
                cart[product_id]['quantity'] = existing_qty + quantity
        else:
            cart[product_id] = {
                'quantity': quantity,
                'size': size,
            }

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart:view_cart')


def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))

        if product_id not in cart:
            return redirect('cart:view_cart')

        if quantity > 0:
            
            if isinstance(cart[product_id], int):
                cart[product_id] = quantity
            else:
                cart[product_id]['quantity'] = quantity
        else:
            cart.pop(product_id, None)

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart:view_cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart:view_cart')
