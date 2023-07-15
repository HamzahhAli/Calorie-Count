from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FoodForm
from .models import Food
from .forms import CalorieLimit
from .models import calLimit
from .forms import *
from .models import *
# Create your views here.

def count(request):
    foods = Food.objects.all() 
    limits = calLimit.objects.all()

    total_calories = 0
    total_protein = 0
    total_fats = 0

    for food in foods:
        total_calories += food.calories
        total_protein += food.protein
        total_fats += food.fats
    

    return render(request, 'calorieapp/count.html', {'foods': foods, 'limit': limits, 'total_calories': total_calories, 'total_protein':total_protein, 'total_fats': total_fats, })

def numbers(request):
    foods = Food.objects.all() 
    limits = calLimit.objects.all()

    total_calories = 0
    total_protein = 0
    
    for food in foods:
        total_calories += food.calories
        total_protein += food.protein

    for limit in limits:
        maxCal = limit
    
    return render(request, 'calorieapp/numbers.html',  {'foods': foods, 'limit': limits, 'total_calories': total_calories, 'total_protein':total_protein, 'maxCal': maxCal })
    


# def graph(request, total_calories, limit):
#     caloriesLeft = limit - total_calories
#     return render(request, 'calorieapp/numbers.html', {'caloriesLeft': caloriesLeft })

def foodinfo(request):
    form = FoodForm()
    form_class = FoodForm
    if request.method == 'POST':
       
        form = FoodForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'calorieapp/foodinfo.html', context)

def CalLimit(request, pk):
    # form = CalorieLimit()
    # if request.method == 'POST':
    #     form = CalorieLimit(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = CalorieLimit()

    calorielimit = calLimit.objects.get(id = pk)
     
    form = CalorieLimit(instance = calorielimit)

    if request.method == 'POST':
        form = CalorieLimit(request.POST, instance = calorielimit)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'calorieapp/calorielimit.html', context )

# def count(request):
#     foods = Food.objects.all() 
#     limit = calLimit.objects.all()
#     return render(request, 'calorieapp/count.html', {'foods': foods, 'limit': limit})

    
    
def deleteItem(request,item_id):
    foodpreset = Food.objects.get(id=item_id)
    foodpreset.delete()
    return redirect('count')






