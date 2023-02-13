from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('contact.html', views.contact, name='contact')
]