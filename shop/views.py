from email.mime import image
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.form import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    all_products = Product.objects.all()

    paginator = Paginator(all_products, 6)

    page = request.GET.get('page')

    p = paginator.get_page(page)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(Paginator.num_pages)

     
    return render(request, 'shop/product/list.html', {
                            'p': p,
                            'products': page,
                            'category': category,
                            'categories': categories, 
                            'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

def search_products(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        products = Product.objects.filter(name__contains=searched)
    return render(request, 'shop/product/search_products.html',
                            {'searched': searched,
                            'products': products})

# Create your views here.
