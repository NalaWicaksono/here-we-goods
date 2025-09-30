import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Product, Item
from .forms  import ProductForm

# ---------- AUTH ----------
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response

# ---------- PRODUCTS (UI TOKO) ----------
@login_required(login_url="/login/")
def product_list(request):
    # ?filter=all | my
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my":
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()

    context = {
        "product_list": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }
    return render(request, "home.html", context)

@login_required(login_url="/login/")
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        messages.success(request, "Product created.")
        return redirect("main:show_main")
    return render(request, "add_product.html", {"form": form})

@login_required(login_url="/login/")
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated.")
            return redirect("main:show_main")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})

@login_required(login_url="/login/")
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted.")
    return redirect("main:show_main")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "detail_product.html", {"product": product})

# ---------- DATA DELIVERY UNTUK Item (tetap seperti tugas sebelumnya) ----------
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
