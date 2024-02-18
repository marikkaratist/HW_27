from django.shortcuts import render
from django.views import View


class AdsView(View):
    def get(self, request):
        return 200, {"status": "ok"}

