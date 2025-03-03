from django.shortcuts import render, redirect
from hospitalapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def starter(request):
    return render(request,'starter-page.html')
def services(request):
    return render(request,'service-details.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def doctors(request):
    return render(request,'doctors.html')
def department(request):
    return render(request,'department.html')
def Appoint(request):
    if request.method == "POST":
       myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
       myappointments.save()
       return redirect('/Appoint')

    else:
        return render(request,'Appointment.html')

def contact(request):
    if request.method == "POST":
        mycontacts = ContactMe(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontacts.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')