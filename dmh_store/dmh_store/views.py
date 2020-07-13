from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import login
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'index.html',{
        #context
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': [
            {'title': 'Playera', 'price': 5, 'stock': True}, # produto
            {'title': 'Camisa', 'price': 7, 'stock': True},
            {'title': 'Mochila', 'price': 20, 'stock': False}
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print('Usuario autenticado')
        else:
            print('Usuario no autenticado')

    return render(request, 'users/login.html', {

    })