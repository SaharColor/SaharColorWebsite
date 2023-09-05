from django.shortcuts import render, redirect
from .models import Product


def GoTOMarket(request):
    return redirect("Market")


def MarketPage(request):
    return render(request, "Home.html")


def ProductsPage(request):
    context = {"Products": Product.objects.all()}
    return render(request, "Products.html", context)


def ProductInfoPage(request, id=0):
    context = {
        "Product": Product.objects.get(id=id)
    }
    return render(request, "Product Info.html", context)


def SearchTry(request):
    SearchText = request.POST["Text"]
    return redirect("Search", Text=SearchText)


def Search(request, Text=""):
    context = {
        "SearchText": Text
    }
    return render(request, "Search.html", context)
