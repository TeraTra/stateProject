from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm

# Create your views here.

#view for page home 
def index_view(request):
    lastProject = Project.objects.last()
    return render(request, 'statApp/index.html', {'projectLast': lastProject})


#view for page add
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


def history_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'statApp/history.html', context)


#view for page update
def update_view(request, project_id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Project, pk = project_id)
 
    # pass the object as instance in form
    form = ProjectForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("allProjects")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "statApp/update.html", context)


#view for page allprojects
def allProject_views(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'statApp/allprojects.html', context)





