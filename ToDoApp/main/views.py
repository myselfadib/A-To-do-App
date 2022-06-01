from cgitb import text
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from . import models
# Create your views here.
def home(request):
    todoItems = models.ToDO.objects.all().order_by("-date")
    return render(request, 'main/index.html', {"todoItems": todoItems})

@csrf_exempt
def  add_todo(request):
    currentDate = timezone.now()
    content = request.POST["content"]
    obj = models.ToDO.objects.create(date = currentDate, text = content)
    print(obj)
    print(obj.id)

    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    models.ToDO.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

