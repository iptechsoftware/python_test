from django.shortcuts import render
from .forms import BuyForm
from .models import Product, Purchase


def home(request):
    products = Product.objects.all().filter(available=True)

    return render(request, 'index.html', {'products': products})


def product_page(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'product.html', {'product': product})


def purchase_item(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    form = BuyForm()
    if product.inventory_on_hand > 0:

        if request.method == "POST":
            form = BuyForm()
            order = Purchase.objects.create(
                product=product,
                customerName=request.POST['Name'],
                emailAddress=request.POST['Email'],
                address=request.POST['Address'],
                phoneNumber=request.POST['Phone']

            )
            order.save()
            product.inventory_on_hand = product.inventory_on_hand - 1
            product.save()
            return render(request, 'purchase_complete.html', {'order': order})

    return render(request, 'cart.html', {'product': product, "form": form})


def search(request):
    products = Product.objects.filter(name__contains=request.GET['name'])
    return render(request, 'index.html', {'products': products})
