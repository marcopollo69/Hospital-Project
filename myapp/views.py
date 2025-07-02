from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def starter(request):
    return render(request,"starter-page.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def doctors(request):
    return render(request,"doctors.html")

def contact(request):
    return render(request,"contact.html")

def departments(request):
    return render(request,"departments.html")

def appointment(request):
    if request.method == "POST":
        myappointments = Appointment1(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date_time = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
        myappointments.save()
        messages.success(request, 'Your appointment has been submitted')
        return redirect('/appointment')

    else:
        return render(request, "appointment.html")

def contact(request):
    if request.method == 'POST':
        mycontacts = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        mycontacts.save()
        messages.success(request, 'Thank you for contacting us')
        return redirect('/contact')
    else:
        return render(request, 'contact.html')