from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Category,TodoList
import datetime

def index(request):
    # todos = TodoList.objects.all() #get all the tasks
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            important = request.POST["imp"]
            date = str(request.POST["date"])
            category =  request.POST["category_select"]
            content = title + "--" + date + " " + category
            Todo = TodoList(title=title, content=content , due_date = date, category = Category.objects.get(name=category),important = important)
            Todo.save()
            return redirect("/index") #reload
        # if "imp" in request.POST:


    return render(request, "index.html", {"categories":categories})

def display(request):
    todos = TodoList.objects.filter(completed = False).order_by('due_date')
    if request.method == "POST":
        if "taskComplete" in request.POST:
            checkedlist = request.POST.get("checkedbox")
            for todo_id in checkedlist:
                # todo = TodoList.objects.get(id=int(todo_id))
                TodoList.objects.filter(id=int(todo_id)).update(completed=True)
        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()

    return render(request,"display.html", {"todos":todos})

def completed(request):
    todos = TodoList.objects.filter(completed = True).order_by('due_date')
    # if request.method == "POST":
    #     if "taskComplete" in request.POST:
    #         checkedlist = request.POST.get("checkedbox")
    #         for todo_id in checkedlist:
    #             # todo = TodoList.objects.get(id=int(todo_id))
    #             TodoList.objects.filter(id=int(todo_id)).update(completed=True)
    #     if "taskDelete" in request.POST:
    #         checkedlist = request.POST["checkedbox"]
    #         for todo_id in checkedlist:
    #             todo = TodoList.objects.get(id=int(todo_id))
    #             todo.delete()

    return render(request,"completed.html", {"todos":todos})
