from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth import  authenticate, login,logout
from django.template import loader, Context, RequestContext
from cookbook.forms import GetRecipe, LoginForm
from django.views.generic.edit import FormView



def all_recipes(request):
    return render(request, 'base_template/all_recipes.html')

def home(request):
    return render(request, 'base_template/base.html')

def show_recipe(request):
    return render(request, 'recipe/show_recipe.html')

def user_cab(request):
    return render(request, 'base_template/users.html')

def get_recipe(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = GetRecipe(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('ok')
            return show_recipe(request)

        else:
            print (form.errors)
            print('not ok')
            return home(request)
    else:
        form = GetRecipe()
        print('xz')
        return render(request, 'recipe/get_recipe.html')

def like_recipe(request):
    recipe_id=request.GET.get('recipe_id', None)
    Rating=0
    if(recipe_id):
        recipe = Recipe.objects.get(id=int(recipe_id))
        if recipe is not None:
            Rating =recipe.Rating + 1
            recipe.Rating = Rating
            recipe.save()

        return HttpResponse(Rathing)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('base_template/base.html')

                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
    return render(request, 'base_template/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("No")
            return HttpResponseRedirect('base_template/login.html')
        else:
            form = UserCreationForm()
            print("yes")
            return render(request, 'base_template/login.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'base_template/registration.html', {'form': form})

    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('base_template/base.html')
