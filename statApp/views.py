from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def index_view(request):
    lastProject = Project.objects.last()
    return render(request, 'statApp/index.html', {'projectLast': lastProject})


def addProject_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
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
