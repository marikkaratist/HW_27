import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad, Category


@method_decorator(csrf_exempt, name='dispatch')
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

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]

        ad.save()

        return JsonResponse({
            "Id": ad.Id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


@method_decorator(csrf_exempt, name="dispatch")
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

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category()
        category.name = category_data["name"]
        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class AdDetailView(View):
    def get(self, request, pk):
        ad_data = get_object_or_404(Ad, Id=pk)

        return JsonResponse({
            "Id": ad_data.Id,
            "name": ad_data.name,
            "author": ad_data.author,
            "price": ad_data.price,
            "description": ad_data.description,
            "address": ad_data.address,
            "is_published": ad_data.is_published
        })


class CategoryDetailView(View):
    def get(self, request, pk):
        cat_data = get_object_or_404(Category, id=pk)

        return JsonResponse({
            "id": cat_data.id,
            "name": cat_data.name
        })
