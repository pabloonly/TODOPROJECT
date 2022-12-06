from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)

    context = {
        "todo_list" : todos 
    }
    return render(request, 'todoapp/todo_list.html', context)

# def todo_list(request):
#     return render(request, 'todo_list2.html')