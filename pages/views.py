from django.shortcuts import render
from products.models import Product

# Create your views here.

def home(request):
    featured_products = Product.objects.all()[:4]

    context = {
        'featured_products': featured_products,
    }

    return render(request, 'pages/home.html', context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_403(request, exception=None):
    return render(request, '403.html', status=403)

def custom_500(request):
    return render(request, '500.html', status=500)
