from django.http import HttpResponse
from django.shortcuts import render
from contactenquiry.models import contactEnquiry

def home(request):
    return render(request, "home.html")


def services(request):
    return render(request, "Services.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('fullName')
        email=request.POST.get('Email')
        number=request.POST.get('number')
        birthDate=request.POST.get('birthDate')
        gendermale=request.POST.get('gender-male')
        genderfemale=request.POST.get('gender-female')
        gendernone=request.POST.get('gender-none')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        place=request.POST.get('place')
        city=request.POST.get('city')
        postalcode=request.POST.get('postalcode')
        en=contactEnquiry(name=name,email=email,phone=number,birthdate=birthDate,gendermale=gendermale,genderfemale=genderfemale,gendernone=gendernone,address1=address1,address2=address2,place=place,city=city,postalcode=postalcode)
        en.save()
    return render(request, "Contact.html")


def gallery(request):
    return render(request, "gallery.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")