from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    people = [
        {'name' : 'Asfandyar', 'age' : 20},
        {'name' : 'Asad', 'age' : 22},
        {'name' : 'Abu Bakar', 'age' : 23},
        {'name' : 'Nadeem Abbas', 'age' : 22},
        {'name' : 'Ahtisham', 'age' : 23}
    ]
    return render(request, 'index.html', context={'people': people})


def success_page(request):
    print('*' * 10)
    return HttpResponse('Hey! This is success page of Django Server...')
