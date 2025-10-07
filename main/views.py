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
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_http_methods
import json
from django.http import JsonResponse


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

# ---------- DATA DELIVERY UNTUK Item ----------
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

def product_list_json(request):
    items = Product.objects.all().values(
        'id','name','price','description','stock','image_url','created_at','user_id'
    )
    return JsonResponse(list(items), safe=False)

def product_detail_json(request, pk):
    try:
        p = Product.objects.values(
            'id','name','price','description','stock','image_url','created_at','user_id'
        ).get(pk=pk)
        return JsonResponse(p)
    except Product.DoesNotExist:
        return JsonResponse({'detail':'Not found'}, status=404)
    
@login_required(login_url="/login/")
def product_page(request):
    return render(request, "home.html", {"last_login": request.COOKIES.get("last_login", "Never")})


def product_to_dict(p: Product):
    return {
        "id": p.id,
        "name": p.name,
        "price": float(p.price) if p.price is not None else 0,
        "description": p.description or "",
        "thumbnail": p.thumbnail or "",
        "category": p.category or "",
        "is_featured": p.is_featured,
        "owner": p.user.username if p.user_id else None,
    }

@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def api_products_list_create(request):
    if request.method == "GET":
        scope = request.GET.get("filter", "all")
        qs = Product.objects.all() if scope != "my" else Product.objects.filter(user=request.user)
        data = [product_to_dict(p) for p in qs.order_by("-id")]
        return JsonResponse({"ok": True, "data": data})
    # POST create (form-urlencoded atau JSON)
    payload = request.POST or json.loads(request.body or "{}")
    form = ProductForm(payload)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return JsonResponse({"ok": True, "data": product_to_dict(obj)}, status=201)
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

@login_required(login_url="/login/")
@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api_products_retrieve_update_delete(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"ok": True, "data": product_to_dict(obj)})

    if request.method in ["PUT", "PATCH"]:
        payload = json.loads(request.body or "{}")
        form = ProductForm(payload, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({"ok": True, "data": product_to_dict(obj)})
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)

    # DELETE
    obj.delete()
    return JsonResponse({"ok": True})

@require_http_methods(["POST"])
def api_login(request):
    payload = request.POST or json.loads(request.body or "{}")
    user = authenticate(request, username=payload.get("username"), password=payload.get("password"))
    if user is None:
        return JsonResponse({"ok": False, "error": "Invalid credentials"}, status=400)
    login(request, user)
    resp = JsonResponse({"ok": True})
    resp.set_cookie("last_login", str(datetime.datetime.now()))
    return resp

@require_http_methods(["POST"])
def api_register(request):
    form = UserCreationForm(request.POST or None)
    if not form.is_valid():
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)
    form.save()
    return JsonResponse({"ok": True})

@require_http_methods(["POST"])
def api_logout(request):
    logout(request)
    resp = JsonResponse({"ok": True})
    resp.delete_cookie("last_login")
    return resp


def product_to_dict(p):
    return {
        "id": p.id,
        "name": p.name,
        "price": float(p.price) if p.price is not None else 0,
        "description": p.description or "",
        "thumbnail": p.thumbnail or "",
        "category": p.category or "",
        "is_featured": p.is_featured,
        "owner": p.user.username if p.user_id else None,
    }

@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def api_products_list_create(request):
    if request.method == "GET":
        scope = request.GET.get("filter", "all")
        qs = Product.objects.all() if scope != "my" else Product.objects.filter(user=request.user)
        data = [product_to_dict(p) for p in qs.order_by("-id")]
        return JsonResponse({"ok": True, "data": data})
    payload = request.POST or json.loads(request.body or "{}")
    form = ProductForm(payload)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return JsonResponse({"ok": True, "data": product_to_dict(obj)}, status=201)
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

@login_required(login_url="/login/")
@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api_products_retrieve_update_delete(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"ok": True, "data": product_to_dict(obj)})

    if request.method in ["PUT", "PATCH"]:
        payload = json.loads(request.body or "{}")
        form = ProductForm(payload, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({"ok": True, "data": product_to_dict(obj)})
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)

    obj.delete()
    return JsonResponse({"ok": True})

