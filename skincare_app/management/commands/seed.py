import json
import requests
from django.core.management.base import BaseCommand
from skincare_assistant.settings import RAPID_API_KEY, RAPID_API_HOST
from ...models import Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        seed_products()
        print("Completed")


def get_products():
    url = "https://sephora.p.rapidapi.com/products/list"
    headers = {
        'X-RapidAPI-Key': RAPID_API_KEY,
        'X-RapidAPI-Host': RAPID_API_HOST,
    }
    querystring = {"categoryId": "cat150006"}
    products = requests.get(url, headers=headers, params=querystring).json()['products']

    url_detail = "https://sephora.p.rapidapi.com/products/detail"

    for product in products:
        product_id = product['productId']
        product_sku = product['currentSku']['skuId']
        querystring = {"productId": {product_id}, "preferedSku": {product_sku}}
        product_details = requests.get(url_detail, headers=headers, params=querystring).json()
        category = product_details['parentCategory']['displayName']
        product['category'] = category

    return products


def seed_products():
    for product in get_products():
        product = Product(
            name=product['displayName'],
            brand=product['brandName'],
            category=product['category'],
            image=product['image450']
        )
        product.save()


