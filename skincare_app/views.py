from django.shortcuts import render
from skincare_app.forms import SearchProductForm
from skincare_app.models import Product


def home(request):
    return render(request, 'skincare_app/home.html')


def search_products(request):
    form = SearchProductForm(request.GET or None)
    products = {}

    if form.is_valid():
        name = form.cleaned_data['name']
        brand = form.cleaned_data['brand']
        category = form.cleaned_data['category']
        products = Product.objects.filter(
            name__icontains=name,
            brand__icontains=brand,
            category__icontains=category
        )

    context = {'form': form, 'products': products}
    return render(request, 'skincare_app/search_products.html', context)

