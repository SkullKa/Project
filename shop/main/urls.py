
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.main, name = 'Main'),
    path('category/<int:id_cat>', views.category, name = 'Category'), 
    path('info', views.info, name = 'info'),
    path('main', views.main, name = 'Main'), 
    path('product/<int:id_prod>', views.product, name = 'Product'),
    path('contact', views.contact, name = 'Contact'),
    ]