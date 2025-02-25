from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def starter(request):
    return render(request,'starterpage.html')
def services(request):
    return render(request,'service-details.html')
