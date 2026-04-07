# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Member, MyTable
from django.db import IntegrityError
from django.contrib import messages

def home(request):
    return HttpResponse("Hello, World!")

def insert_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")

        try:
            MyTable.objects.create(name=name, subject=subject, email=email)
            messages.success(request, "Data inserted successfully")
        except IntegrityError:
            messages.error(request, "Email already exists")
            return render(request, "form.html", {"error": "Email already exists"})
        return redirect("insert")

    return render(request, "form.html")

def form_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')

        MyTable.objects.create(
            name=name,
            subject=subject,
            email=email
        )

    return render(request, 'form.html')

def show_data(request):
    data = MyTable.objects.all()
    return render(request, 'show.html', {'data': data})
