from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm

def index(request):
    if request.POST:
        form = ResumeForm(request.POST)
        form.save()
        return redirect("resumes:index")
    
    resumes = Resume.objects.order_by("-id")
    return render(request, "resumes/index.html", {"resumes": resumes})

def new(request):
    form = ResumeForm
    return render(request, "resumes/new.html", {"form": form})

def show(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.POST:
        form = ResumeForm(request.POST, instance=resume)
        form.save()
        return redirect("resumes:index")
    
    return render(request, "resumes/show.html", {"resume": resume})

def edit(request, id):
    resume = get_object_or_404(Resume, id=id)
    form = ResumeForm(instance=resume)
    return render(request, "resumes/edit.html", {"resume": resume, "form": form})

def delete(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.POST:
        resume.delete()
        return redirect("resumes:index")
    
    return render(request, "resumes/delete.html", {"resume": resume})