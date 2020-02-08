

"""these are the products urls"""

from django.contrib import admin
from django.urls import path,include
from .views import product_views
urlpatterns = [
    path('',product_views,name="home"),
]