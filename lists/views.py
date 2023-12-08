from django.shortcuts import render
from typing import Type
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def home_page(request: Type[HttpRequest]):
    return HttpResponse('<html><title>To-Do Lists</title></html>')