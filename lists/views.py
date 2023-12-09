from django.shortcuts import redirect, render
from typing import Type
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item

# Create your views here.
def home_page(request: Type[HttpRequest]):

    if request.method == 'POST':
        Item.objects.create(text=request.POST['new-item-input'])
        return redirect('/')
    
    return render(
        request, 
        'home.html',
        {'new_item': request.POST.get("new-item-input", "")}
    )