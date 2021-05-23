from django.shortcuts import render, get_object_or_404, render_to_response
from product.models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart
from datetime import datetime

# Страница с товарами
def ProductList(request, category_slug=None):
    cart = Cart(request)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {
    	'title': 'Все товары',
    	'cart': cart,
        'category': category,
        'categories': categories,
        'products': products,
        'year':datetime.now().year,
    })

# Страница товара
def ProductDetail(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html',
                             {
                             	'title': 'Товар',
                             	'cart': cart,
                             	'product': product,
                                'cart_product_form': cart_product_form,
                                'year':datetime.now().year,
                             }
                  )
