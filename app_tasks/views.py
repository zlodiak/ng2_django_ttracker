from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json

from .models import Task, Status

def index(request):
  tasks = Task.objects.all()   
  tasks_serialized = serializers.serialize('json', tasks)
  return JsonResponse(tasks_serialized, safe=False) 


def all_statuses(request):
  statuses = Status.objects.all()   
  statuses_serialized = serializers.serialize('json', statuses)
  return JsonResponse(statuses_serialized, safe=False)   