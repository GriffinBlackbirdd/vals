from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'landing/index.html')
def thoughts(request):
    return render(request, 'landing/thoughts.html')
def ilikeyou(request):
    return render(request, 'landing/ilikeyou.html')
def image_flip(request):
    return render(request, 'landing/image_flip.html')
def contact(request):
    return render(request, 'landing/contact.html')

