from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, world. You're at the start page.")
