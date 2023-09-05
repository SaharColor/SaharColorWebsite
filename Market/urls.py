from django.urls import path
from . import views

urlpatterns = [
    path("", views.GoTOMarket, name="GoToMarket"),
    path("Market/", views.MarketPage, name="Market"),
    path("Market/Products/", views.ProductsPage, name="Products"),
    path("Market/Product/<int:id>/", views.ProductInfoPage, name="ProductInfo"),
    path("Market/Search/Try/", views.SearchTry, name="SearchTry"),
    path("Market/Search/<str:Text>/", views.Search, name="Search"),
]
