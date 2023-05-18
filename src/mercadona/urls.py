from django.urls import path
from . import views

urlpatterns = [
    path('', views.mercadona_list, name="home"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('delete/<product_id>', views.delete_product, name="delete"),
    path('produit/new/', views.produit_new, name='produit_new'),
    path('promo_new/', views.promo_new, name='promo_new'),


]