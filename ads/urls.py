from django.urls import path
from ads import views

urlpatterns = [
    path("ad/", views.AdsView.as_view(), name="ad"),
    path("category/", views.CategoriesView.as_view(), name="category"),
    # path("ad/<int:pk>", views.AdsView.as_view())
]
