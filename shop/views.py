from multiprocessing import context
from os import remove
from unicodedata import category
from django.http import HttpResponse, JsonResponse
from .models import Product, Order, OrderItem, ContactForm
from .models import Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.conf import settings
import random
from django.views.decorators.csrf import csrf_exempt


def home(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'home.html', {'cart': cart})


def bedroom(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    if bedroom:
        products = Product.objects.filter(category=1)
        return render(request, 'bedroom.html', {'product': products, 'category': 1, 'cart': cart})


def livingroom(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    if livingroom:
        products = Product.objects.filter(category=2)
        return render(request, 'livingroom.html', {'product': products, 'category': 2, 'cart': cart})


def diningroom(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    if diningroom:
        products = Product.objects.filter(category=3)
        return render(request, 'diningroom.html', {'product': products, 'category': 3, 'cart': cart})


def bedding(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    if bedding:
        products = Product.objects.filter(category=4)
        return render(request, 'bedding.html', {'product': products, 'category': 4, 'cart': cart})


def youth(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    if youth:
        products = Product.objects.filter(category=5)
        return render(request, 'youth.html', {'product': products, 'category': 5, 'cart': cart})


def newarrival(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    products = Product.objects.all()
    return render(request, 'newarrival.html', {'product': products, 'cart': cart})


def login(request):
    return render(request, 'login.html')


def signup(request):

    if request.method == "POST":
        # Get the Post Parameter
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect("signup")
            else:
                # Create User
                user = User.objects.create_user(username=username,
                                                first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                return redirect("login")

        else:
            messages.info(request, "Password not matching")
            return redirect("signup")

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect("home")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def product(request, id):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    products = Product.objects.filter(id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product.html', {'product': products, 'cart_product_form': cart_product_form, 'cart': cart})


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required(login_url='login')
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        neworder = Order()
        current_user = request.user
        neworder.user = User.objects.get(id=current_user.id)
        neworder.name = request.POST.get('name')
        neworder.address = request.POST.get('address')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.zip_code = request.POST.get('zip_code')

        neworder.payment_mode = request.POST.get('payment_mode')

        cart = Cart(request)
        cart.get_total_price=0
        for item in cart:
            cart.get_total_price = cart.get_total_price+ item['price']*item['quantity']

            neworder.total_price = cart.get_total_price
            trackingno = 'DreamDecor_' + str(random.randint(1111111, 9999999))
            while Order.objects.filter(tracking_no=trackingno) is None:
                trackingno = 'DreamDecor_' + \
                    str(random.randint(1111111, 9999999))

            neworder.tracking_no = trackingno
            neworder.save()

            neworderitems = Cart(request)
            for item in neworderitems:
                OrderItem.objects.create(order=neworder,
                                         product=item['product'],
                                         price=item['total_price'],
                                         quantity=item['quantity'])

            cart.clear()
        messages.info(request, "Your Order has been successfully placed.")
        return redirect('/cart_detail')


@csrf_exempt
def payment_done(request):
    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_cancelled(request):
    return render(request, 'paypal/payment_cancelled.html')


def payment_process(request):
    return render(request, 'paypal/payment_process.html')


def order(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'cart/order.html', context)


def orderview(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(
        user=request.user).first()
    orderitem = OrderItem.objects.filter(order=order)
    context = {'order': order, 'orderitem': orderitem}
    return render(request, 'cart/orderview.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        newcontact = ContactForm()
        current_user = request.user
        newcontact.user = User.objects.get(id=current_user.id)
        newcontact.name = request.POST.get('name')
        newcontact.phone = request.POST.get('phone')
        newcontact.email = request.POST.get('email')
        newcontact.phone = request.POST.get('phone')
        newcontact.subject = request.POST.get('subject')
        newcontact.message = request.POST.get('message')
        newcontact.save()

        messages.success(request, "Thank You for contacting us.")
    return render(request, 'contact.html')
