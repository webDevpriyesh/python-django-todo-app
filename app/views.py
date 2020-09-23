from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import TodoList

# Create your views here.

def index(request):
    todo_lists = TodoList.objects.all().order_by("-pub_date")
    return render(request, 'index.html', {'todo_lists':todo_lists})




def add_todo(request):
    todo_item = request.POST.get('name')
    TodoList.objects.create(text=todo_item)
    return HttpResponseRedirect(reverse('index'))

def delete_todo(request, todo_id):
    TodoList.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('index'))
