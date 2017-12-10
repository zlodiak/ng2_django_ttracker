from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json

from .models import Task

def index(request):
  tasks = Task.objects.all()   
  tasks_serialized = serializers.serialize('json', tasks)
  return JsonResponse(tasks_serialized, safe=False) 