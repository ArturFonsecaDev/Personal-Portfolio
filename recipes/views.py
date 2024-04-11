from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.


def home_page(req): return render(req, 'recipes/index.html')


def processing_forms(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        msg = req.POST.get('message')
        send_mail(
            f'Subject: Thanks for contacting. Your message just arrived at my mail box, in no time you will get an answer!',
            f'I read your following request, and will answer soon, thanks for the time!\n{msg}',
            'sgsartur@hotmail.com',  # Usar o email do remetente
            [email],  # Enviar para o email do usuário
            fail_silently=False,
        )
        send_mail(
            f'{name} wanna discuss about a project',
            f'This is {name} request:\n{msg}',
            'sgsartur@hotmail.com',
            ['sgsartur@hotmail.com'],
            fail_silently=False,
        )
    return HttpResponseRedirect('/')
