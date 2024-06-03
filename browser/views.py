from django.shortcuts import render,redirect
from . forms import TodoForm
from . models import Todo
def index(request):
    data=Todo.objects.all()
    to=TodoForm()
    data ={
        "to":to,
        "data":data
    }
    if request.method=="POST":
        todo=TodoForm(request.POST)
        if todo .is_valid():
            todo.save()
            return redirect("home")
    return render(request,"index.html",data)
def delete(request,id):
    item=Todo.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect("home")
def update(request,id):
    data1=Todo.objects.get(id=id)
    to=TodoForm(instance=data1)
    data ={
        "to":to
    }
    if request.method=='POST':
        form = TodoForm(request.POST, instance=data1)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"update.html",data)

    
