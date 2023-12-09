from django.shortcuts import render
from typing import Type
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request: Type[HttpRequest]):
    return render(request, 'home.html')