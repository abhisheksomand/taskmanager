from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_tasks(request):
    tasks= Task.objects.filter(assigned_to=request.user)
    serilaizer = TaskSerializer(tasks,many=True)
    return Response(serilaizer.data)

@api_view(['PUT'])
def update_task(request,id):
    tasks= Task.objects.get(id=id)
    serilaizer = TaskSerializer(tasks,data=request.data)
    if serilaizer.is_valid():
        serilaizer.save()

    return Response(serilaizer.data)

@api_view(['GET'])
def task_report(request,id):
    tasks = Task.objects.get(id=id)
    data= {
        "completion_report":tasks.completion_report,
        "worked_hours":tasks.worked_hours
    }
    return Response(data)