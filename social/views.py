from django.shortcuts import render, HttpResponse, redirect
from social.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginUserForm , ProductForm
from django.utils.text import slugify

from products.models import Products

# Create your views here.

def home(request):
    context = {}
    return render(request, 'social/index.html', context)


def become_vendor(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('vendor-admin')

    else:
        form = CreateUserForm()

    context = {'form':form}

    return render(request, 'social/register.html', context)


@login_required()
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    return render(request, 'social/vendor-admin.html', {'vendor': vendor, 'products': products })


@login_required()
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor-admin')
    else:
        form = ProductForm()

    return render(request, 'social/add_product.html', {'form': form})


def login_user(request):

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
    else:
        form = LoginUserForm()

    context = {'form': form}
    return render(request, 'social/login.html', context)


def base(request):
    context = {}
    return render(request, 'social/base.html', context)


def post_add(request):
    context = {}
    return render(request, 'social/post_add.html', context)


def vendor_admin(request):
    context = {}
    return render(request, 'social/vendor-admin.html', context)


def test_post(request):
    context = {}
    return render(request, 'social/test_post.html', context)


def blank(request):
    context = {}
    return render(request, 'social/blank.html', context)


def testh(request):
    context = {}
    return render(request, 'social/test_home.html', context)


def main(request):
    context = {}
    return render(request, 'social/main.html', context)


def testbase(request):
    context = {}
    return render(request, 'social/bhome.html', context)


def login(request):
    context = {}
    return render(request, 'social/login.html', context)


def testlogin(request):
    context = {}
    return render(request, 'social/testlogin.html', context)


def register(request):
    context = {}
    return render(request, 'social/register.html', context)


def add_product(request):
    context = {}
    return render(request, 'social/add_product.html', context)


def cart(request):
    context = {}
    return render(request, 'social/cart.html', context)


def landing(request):
    context = {}
    return render(request, 'social/landing.html', context)


def footer(request):
    context = {}
    return render(request, 'social/footer.html', context)


def signup(request):
    context = {}
    return render(request, 'social/signup.html', context)


def products(request):
    context = {}
    return render(request, 'social/products.html', context)


def home_page(request):
    context = {}
    return render(request, 'social/lan2.html', context)


def view_product(request):
    context = {}
    return render(request, 'social/view_product.html', context)