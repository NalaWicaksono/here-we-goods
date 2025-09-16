from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Item                 
from .forms import ItemForm

# 1. Halaman daftar + tombol Add dan Detail
def show_items(request):
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})

# 2. Form tambah item
def add_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():          # wajib: validasi form (lihat penjelasan di bawah)
            form.save()
            return redirect("show_items")
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
