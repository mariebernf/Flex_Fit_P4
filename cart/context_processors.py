from products.models import Product

def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0

   
    products = Product.objects.filter(id__in=cart.keys())

    for product in products:
        item = cart[str(product.id)]
        quantity = item['quantity']
        size = item['size']

        total += product.price * quantity
        product_count += quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'size': size,
        })

    return {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }
