from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    template = loader.get_template('home.html')
    context = {
        'name': "Satyam Mishra",
        "email": "satyam@gmail.com",
        "address": "Bangalore",
    }
    return HttpResponse(template.render(context, request))
