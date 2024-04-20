from django.shortcuts import render,redirect
from .models import *
from recipies_project.settings import BASE_DIR
# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    recipies = recipies_data.objects.all()
    return render(request, 'index.html', {'recipies':recipies, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        recipie = recipies_data()
        recipie.recipie_name = request.POST.get('recipie_name',False)
        recipie.recipie_description = request.POST.get('recipie_description',False)
        recipie.recipie_duration = request.POST.get('recipie_duration',False)
        recipie.recipie_ingredients = request.POST.get('recipie_ingredients',False)
        recipie.recipie_steps = request.POST.get('recipie_steps',False)
        recipie.recipie_photo = request.FILES.get("recipie_photo", False)
        recipie.save()

    
    return render(request, 'upload.html')

def add_comment(request, recipie_id):
    if request.method == 'POST':
        recipe = recipies_data.objects.get(pk=recipie_id)
          # Get the comment from the form
        comment_text = request.POST.get('comment_text', '')
        # Add the comment to the recipe
        recipe.comments.create(text=comment_text)
    return redirect('index')