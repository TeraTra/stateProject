from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
def index_view(request):
    lastProject = Project.objects.last()
    return render(request, 'statApp/index.html', {'projectLast': lastProject})

def addProject_view(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/home/')
    else:
        form = ProjectForm()
    context = {
        'forms':form,
    }

    return render(request, "statApp/add.html", context)
