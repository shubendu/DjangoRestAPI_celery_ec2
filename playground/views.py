from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer



def say_hello(request):


    #query_set = Product.objects.filter(last_update__year=2021)

    products = Product.objects.values_list("id","title","collection__title")

    #query_set = Product.objects.filter(title__icontains='coffee')

    return render(request,"hello.html", {"name":"shubendu", "products": list(products)})