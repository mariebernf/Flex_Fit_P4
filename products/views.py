from django.shortcuts import render, get_object_or_404
from .models import Product
from reviews.models import Review

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_on')

    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            product=product,
            user=request.user
        ).first()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'user_review': user_review,
    })
