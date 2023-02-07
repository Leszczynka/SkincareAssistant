import requests
from django.contrib import messages
from django.shortcuts import render
from skincare_assistant.settings import RAPID_API_KEY, RAPID_API_HOST
from .forms import SearchProductsForm


def home(request):
    return render(request, 'skincare_app/home.html')


def search_products(request):
    form = SearchProductsForm(request.GET or None)
    products = {}

    if form.is_valid():
        product_category = form.cleaned_data['product_category']
        skin_type = form.cleaned_data['skin_type']
        querystring = {'q': f'{product_category}, {skin_type}', 'node': '1050055'}
        url = f'https://sephora.p.rapidapi.com/products/search'
        headers = {
            'X-RapidAPI-Key': RAPID_API_KEY,
            'X-RapidAPI-Host': RAPID_API_HOST,
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            products = response.json()
        except requests.exceptions.RequestException:
            messages.error(request, 'An error occurred while searching for products')

    context = {
        'form': form,
        'products': products
    }
    return render(request, 'skincare_app/search_products.html', context)
