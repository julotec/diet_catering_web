from django.shortcuts import render
from django.http import HttpResponse
from Home_App.models import Order_Diet
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def order(request):
    if request.method == "POST":
        name = request.POST.get("name").strip()
        email = request.POST.get("email").strip()
        number= request.POST.get("number").strip()
        variant = request.POST.get("variant").strip()
        kcal = request.POST.get("kcal").strip()
        date = request.POST.get("date").strip()

        print("Name:", name)
        print("Email:", email)
        print("Number:", number)
        print("Variant:", variant)
        print("Kcal:", kcal)
        print("Date:", date)

        if name != '' and email != "" and number != '' and variant != '' and kcal != '' and date != '':
            data = Order_Diet(Name = name, Email = email, Date = date, Kcal = kcal, Variant = variant, Number = number)
            data.save()
            return HttpResponse("Dane zostały pomyślnie zapisane!")
        else:
            return HttpResponse("Wypełnij wszystkie wymagane pola!")
    return render(request, 'order.html')





