# main/views.py
from django.shortcuts import render

def home(request):
    context = {
        "app_name": "Here We Goods",
        "student_name": "Nalakrishna Abimanyu Wicaksono",
        "student_class": "PBP F",
    }
    return render(request, "home.html", context)
