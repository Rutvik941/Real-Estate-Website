from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
  return render(request,'index.html')
   #  return HttpResponse("this is homepage")
    
def contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      review = request.POST.get('review')
      contact = Contact(name=name, email=email, phone=phone, review=review, date=datetime.today())
      contact.save()
      messages.success(request, 'Your Review has been Sent!')
    return render(request,'contact.html')
# return HttpResponse("this is contact page")    

def about(request):
    return render(request,'about.html')
  # return HttpResponse("We Are Bunkers")    
    
def members(request):
    return render(request,'members.html')
  # return HttpResponse("I Am a Member")    
  