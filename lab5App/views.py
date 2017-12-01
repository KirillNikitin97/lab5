from django.shortcuts import render
from random import randint
from datetime import date

# Create your views here.

userss = [
        {'id': 1, 'surname': 'Никитин', 'name': 'Кирилл', 'db': date(1995,5,4), "sex": 'M'},
        {'id': 2, 'surname': 'Попова', 'name': 'Марина', 'db': date(1997,2,4), "sex": 'F'},
        {'id': 3, 'surname': 'Гунькин', 'name': 'Михаил', 'db': date(1999,1,4), "sex": 'M'},
        {'id': 4, 'surname': 'Маркарян', 'name': 'Росанна', 'db': date(1994,5,4), "sex": 'F'},
    ]


contex = {'users': userss}


def main(request):
    return render(request, 'main.html',  contex)


def users(request, id):
    print("ddddd")
    us = userss[int(id)-1]
    cont = {'user': us}
    return render(request, 'users.html', cont)
