
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):

    return render(request, 'landing/index.html')

def contact(request):
    if request.method == 'POST':
        contact=Contact()
        message_name=request.POST.get['name']
        message_email=request.POST.get['email']
        message_subject=request.POST.get['subject']
        send_mail(
            "Message From " + message_name,
            message_subject,
            message_email,
            ['hamidarreyan@gmail.com']
        )
        contact.name=message_name
        contact.email=message_email
        contact.subject=message_subject
        contact.save()
        return HttpResponse("<h1>OMG HIII BEAUTIFUL, DONE, you better must have added that 3 word magical phrase mhm, or soemthing bad will happen.</h1>")
    else:
        return render(request, 'landing/contact.html', {})