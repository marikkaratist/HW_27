from django.urls import path
from ads import views

urlpatterns = [
    path("ad/", views.AdsView.as_view(), name="ad"),
    path("cat/", views.CategoriesView.as_view(), name="category"),
    path("ad/<int:pk>", views.AdDetailView.as_view()),
    path("cat/<int:pk>", views.CategoryDetailView.as_view())
]
