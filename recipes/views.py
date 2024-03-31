from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home_page(req): return render(req, 'template/index.html' )