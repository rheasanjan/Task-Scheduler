"""Author - Rhea Sanjan B.R """

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Category,TodoList
import datetime
from django.utils import timezone

def index(request):
    categories = Category.objects.all() #get all the categories from the table
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            # important = request.POST["imp"]
            imp = request.POST.get("checkedbox")
            if imp:
                important = True
            else:
                important = False
            date = str(request.POST["date"])
            category =  request.POST["category_select"]
            content = title + "--" + date + " " + category # more details
            Todo = TodoList(title=title, content=content , due_date = date, category = Category.objects.get(name=category),important = important)
            Todo.save() #insert the new task
            return redirect("/index") #reload
    return render(request, "index.html", {"categories":categories})

def display(request):
    #get pending tasks
    todos = TodoList.objects.filter(completed = False).order_by('due_date')
    today = datetime.date.today()

    for t in todos:
        if today > t.due_date:
            missed = TodoList.objects.filter(id=int(t.id)).update(missed_deadline = True)
    if request.method == "POST":
        if "taskComplete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox") #get the selected tasks
            for todo_id in checkedlist:
                TodoList.objects.filter(id=int(todo_id)).update(completed = True) #set completed column to True
            # return redirect("/display")

        if "taskDelete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox")
            for todo_id in checkedlist:
                todo = TodoList.objects.filter(id=int(todo_id))
                todo.delete()
            return redirect("/display")

    return render(request,"display.html", {"todos":todos})

def category(request):
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            name = request.POST["category"]
            cat = Category(name=name)
            cat.save()
            return redirect("/category")
        if "taskDelete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox")
            for cat_id in checkedlist:
                cate = Category.objects.filter(id=int(cat_id))
                cate.delete()
            return redirect("/category")
    return render(request,"addcategories.html",{"categories":categories})


def completed(request):
    todos = TodoList.objects.filter(completed = True).order_by('due_date')

    return render(request,"completed.html", {"todos":todos})
