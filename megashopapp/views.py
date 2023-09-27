from django.shortcuts import render
from shop.models import Product
from shop.models import ReviewRating
# from django.shortcuts import render
# from django.views.generic import TemplateView



def home(request):
    reviews = ()
    products = Product.objects.all().filter(is_avaliable=True).order_by('-created_date')
    for product in products:
        reviews = ReviewRating.objects.get(product_id=product.id, status=True)
    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, "home.html", context)








