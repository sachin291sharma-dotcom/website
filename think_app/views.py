from django.shortcuts import render
from .models import Contact,Enrollment


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def course(request):
    return render(request,"course.html")

def contact(request):
    if request.method =="POST":
        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            message=request.POST["message"],
        )
    return render(request,"contact.html")


def enroll_view(request):
    if request.method == "POST":
        Enrollment.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            course=request.POST['course']
        )
    return render(request, 'enroll.html')

def review(request):
    return render(request,"review.html")