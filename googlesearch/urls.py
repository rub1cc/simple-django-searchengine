from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('search', SearchView.as_view(), name="google-search-view")
]
