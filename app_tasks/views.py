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


def user_tasks(request):
  user_id = request.GET['user_id']
  tasks = Task.objects.filter(user_id=user_id)
  tasks_serialized = serializers.serialize('json', tasks) 
  return JsonResponse(tasks_serialized, safe=False) 


def get_task(request):
  task_id = request.GET['pk']
  task = Task.objects.filter(id=task_id)
  task_serialized = serializers.serialize('json', task) 
  return JsonResponse(task_serialized, safe=False)   


def update_task(request): 
  task_id = request.GET['task_id']
  user_id = request.GET['user_id']
  Task.objects.filter(pk=task_id).update(user=user_id)
  data = json.dumps({ 'request_status': 1 , 'error_id': '', 'error_message': '' })
  return JsonResponse(data, safe=False)     


def update_status(request): 
  task_id = request.GET['task_id']
  status_id = request.GET['status_id']
  Task.objects.filter(pk=task_id).update(status=status_id)
  data = json.dumps({ 'request_status': 1 , 'error_id': '', 'error_message': '' })
  return JsonResponse(data, safe=False)       