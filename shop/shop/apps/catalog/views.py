from django.shortcuts import render
from .models import Product, Category
from cart.forms import CartAddProductForm


def product(request):
    list_category = Category.objects.all()
    return render(request, 'category.html', context={'category': list_category})


def detail(request, category_id, product_id):
    products_code = Product.objects.get(id=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product.html', context={'product': products_code, 'cart_product_form': cart_product_form})


def catalog(request, category_id):
    print(category_id)
    list_product = Product.objects.filter(category_id=category_id)
    return render(request, 'catalog/base.html', context={'product': list_product})
from django.shortcuts import render
from .forms import ImageForm


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})