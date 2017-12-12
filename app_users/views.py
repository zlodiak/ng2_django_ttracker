from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json

from .models import User

def index(request):
  users = User.objects.all()   
  users_serialized = serializers.serialize('json', users)
  return JsonResponse(users_serialized, safe=False) 

def get_user(request):
  user_id = request.GET['id']
  user = User.objects.filter(id=user_id)
  user_serialized = serializers.serialize('json', user) 
  return JsonResponse(user_serialized, safe=False)   

