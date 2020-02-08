from django.shortcuts import render
from django.http import HttpResponse

from .models import product_models

# Create your views here.

def product_views(request):

    products=product_models.objects.all()

    context={
        'products':products,
    }
    return render(request,'base.html',context)


