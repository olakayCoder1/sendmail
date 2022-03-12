import email
from pickle import FROZENSET
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        username = request.POST['username']
        user_mail = request.POST['email']
        if form.is_valid():
            form.save()
            template = render_to_string('client/welcome.html', {'username': username })
            email = EmailMessage(
                'Olakay',
                template,
                to=[
                    user_mail
                ]
            )
            email.send()
            return HttpResponse('CHECK YOUR MAIL FOR MORE INFO')
        else:
            return HttpResponse('Un')

    else:
        form = UserRegistrationForm()
        return render(request, 'client/home.html', {'form': form })