from django.shortcuts import render, redirect
from vege.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def recipes(request):  # sourcery skip: extract-method
    if request.method == 'POST':
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
    
    
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )
        return redirect('/recipes/')
    


    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {'recipes':queryset}
    return render(request, 'recipes.html', context)


@login_required(login_url='/login/')
def delete_recipe(request, id):  # sourcery skip: extract-method
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')


@login_required(login_url='/login/')
def update_recipe(request, id):  # sourcery skip: extract-method
    queryset = Recipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST


        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')  

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description      

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')

    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
        
    

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return render(request, 'login.html')



def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    username = request.POST.get('username') 




    if username_exists := User.objects.filter(username=username).exists():
        messages.error(request, 'Username already exists.')
        return redirect('/register/')

    # Create the user with the provided data
    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password
    )

    messages.success(request, 'Account created successfully.')
    return redirect('/register/')  # Redirect to the register page after successful registration