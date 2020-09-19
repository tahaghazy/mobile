from django.urls import path
from .views import (
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView
)
from . import views
from .views import contactView, successView

app_name = 'core'
from core.sitemaps import  PostSitemap,StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from .views import *
sitemaps = {
    'post': PostSitemap,
    'static':StaticViewSitemap
}
urlpatterns = [
    path('',home, name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('searchposts/', views.searchposts, name='searchposts'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="sitemap"),

]
