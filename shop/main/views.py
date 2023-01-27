from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Order
from django.forms import ModelForm
# Create your views here.

def category(response, id_cat):
	# data = Product.objects.all()
	data = Product.objects.filter(category_id = id_cat)
	cat_name = Category.objects.get(category_id = id_cat)
	return render(response, "main/category.html", {"data": data, "name": cat_name.name})

def main(response):
	data = Category.objects.all()
	return render(response, "main/main.html", {"categories": data})

def info(response):
	# return HttpResponse("<h1> Hello world ! </h1>")
	# return HttpResponse("<h1> Моя жена самая замечательная!!! </h1>")
	return render(response, "main/info.html")
	
data = {'name':'product 1', 'descr':'description of the product', 'price':100}
def product(response, id_prod):
	data = Product.objects.get(id = id_prod)
	# data = {'name':'product 1', 'descr':'description of the product', 'price':100}
	return render(response, "main/product.html", {'product': data})

def contact(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
	form = OrderForm()
	data = {'form': form}
	return render(request, 'main/contact.html', data)