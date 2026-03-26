from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from .models import WishlistItem


@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist/wishlist.html', {
        'wishlist_items': wishlist_items,
    })


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('products:product_detail', product_id=product.id)


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    wishlist_item.delete()
    return redirect('wishlist:wishlist')
