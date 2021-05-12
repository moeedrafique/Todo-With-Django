from django.shortcuts import render
from .forms import TaskForm
from . models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form, "tasks":tasks}
    return render(request, 'home.html', context)

def Update(request):
