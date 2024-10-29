from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def menu(request):
    template = loader.get_template("manu.html")
    return HttpResponse(template.render())

def show_all_company(request):
    company = Company.objects.all()
    return render(request, "allcompany.html", {"companies":company})

def create_company(request):
    if request.method == 'POST':
        form = ComapanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allcompany")
    else:
        form = ComapanyForm()
    return render(request, 'create_company.html', {"form":form})


def update_company(request, pk):
    company = Company.objects.filter(id=pk).first()
    if company:
        if request.method == 'POST':
            form = ComapanyForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                form.save()
                return redirect("allcompany")
        else:
            form = ComapanyForm(instance=company)
    else:
        HttpResponse("NOT FOUND")
    return render(request, 'update_company.html', {"form":form})


def delete_company(request, pk):
    company = Company.objects.filter(id=pk).first()
    if company:
        if request.method == 'POST':
            company.delete()
            return redirect('allcompany')
        return render(request, 'delete_company.html', {'company': company})
    else:
        return HttpResponse('company not found')



def getcomp_by_id(request, pk):
    company = Company.objects.filter(id=pk).first()
    if company:
        return render(request, "getcomp_by_id.html", {"company":company})
    else:
        return HttpResponse("NOT FOUND")
    


def show_all_car(request):
    car = Car.objects.all()
    return render(request, "allcar.html", {"car":car})

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allcar")
    else:
        form = CarForm()
    return render(request, 'create_car.html', {"form":form})


def update_car(request, pk):
    car = Car.objects.filter(id=pk).first()
    if car:
        if request.method == 'POST':
            form = CarForm(request.POST, request.FILES, instance=car)
            if form.is_valid():
                form.save()
                return redirect("allcar")
        else:
            form = CarForm(instance=car)
    else:
        HttpResponse("NOT FOUND")
    return render(request, 'update_car.html', {"form":form})


def delete_car(request, pk):
    car = Car.objects.filter(id=pk).first()
    if car:
        if request.method == 'POST':
            car.delete()
            return redirect('allcar')
        return render(request, 'delete_car.html', {'car': car})
    else:
        return HttpResponse('car not found')



def getcar_by_id(request, pk):
    car = Car.objects.filter(id=pk).first()
    if car:
        return render(request, "getcar_by_id.html", {"car":car})
    else:
        return HttpResponse("NOT FOUND")
    