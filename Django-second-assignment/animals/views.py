from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from animals import models 
@csrf_exempt
def mammals(request):
    if request.method=="GET":
        entries=models.Mammal.objects.all()
        data=[]
        for entry in entries:
            data1=[entry.name,entry.species,entry.gender,entry.food]
            data.append(data1)
        return JsonResponse({"data":data})
            
    if request.method=="POST":
        new_mammal=json.loads(request.body)
        models.Mammal.objects.create(name=new_mammal["name"],species=new_mammal["species"],gender=new_mammal["gender"].upper(),food=new_mammal["food"])
        return JsonResponse({"Created":{"name":new_mammal["name"]}})
    

@csrf_exempt
def birds(request):
    if request.method=="GET":
        entries=models.Bird.objects.all()
        data=[]
        for entry in entries:
            data1=[entry.name,entry.species,entry.food]
            data.append(data1)
        return JsonResponse({"data":data})
            
    if request.method=="POST":
        new_bird=json.loads(request.body)
        models.Bird.objects.create(name=new_bird["name"],species=new_bird["species"],food=new_bird["food"])
        return JsonResponse({"Created":{"name":new_bird["name"]}})
   
@csrf_exempt
def fishes(request):
    if request.method=="GET":
        entries=models.Fish.objects.all()
        data=[]
        for entry in entries:
            data1=[entry.color,entry.species,entry.food,entry.count]
            data.append(data1)
        return JsonResponse({"data":data})
            
    if request.method=="POST":
        new_fish=json.loads(request.body)
        models.Fish.objects.create(color=new_fish["color"],species=new_fish["species"],food=new_fish["food"],count=new_fish["count"])
        return JsonResponse({"Created":{"species":new_fish["species"]}})

