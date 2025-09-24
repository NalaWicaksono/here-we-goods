import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Item                 
from .forms import ItemForm, ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product


# 1. Halaman daftar + tombol Add dan Detail
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login') 
    return render(request, 'register.html', {'form': form})
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '240123456',               
        'name': request.user.username,    
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),  
    }
    return render(request, "home.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)  # sesuai tutorial
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    return render(request, "add_item.html", {'form': form})

def show_items(request):
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})

# 2. Form tambah item
@login_required(login_url="/login")
def add_item(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)  # sesuai tutorial: commit=False
            obj.user = request.user        # relasikan ke user yang login
            obj.save()
            return redirect("main:show_main")
    else:
        form = ProductForm()
    return render(request, "add_item.html", {"form": form})

# 3. Halaman detail item
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, "detail_item.html", {"item": item})

# 4. Data delivery (JSON & XML)
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json",
    )

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml",
    )

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json",
    )

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml",
    )
