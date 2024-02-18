import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from ads.models import Ad, Category


class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()
        search_text = request.GET.get("text", None)
        if search_text:
            ads = ads.filter(text=search_text)
        response = []
        for ad in ads:
            response.append({
                "Id": ad.Id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            })

        return JsonResponse(response, safe=False), 200, {"status": "ok"}

    def post(self, request):
        ad_data = json.loads(request.body)

        new_ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
        )
        return JsonResponse({
            "Id": ad_data.Id,
            "name": ad_data.name,
            "author": ad_data.author,
            "price": ad_data.price,
            "description": ad_data.description,
            "address": ad_data.address,
            "is_published": ad_data.is_published
        })


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        search_text = request.GET.get("text", None)
        if search_text:
            categories = categories.filter(text=search_text)
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False), 200, {"status": "ok"}

    def post(self, request):
        category_data = json.load(request.body)

        new_category = Category.objects.create(
            name=category_data["name"],
        )
        return JsonResponse({
            "name": category_data.name,
        })
