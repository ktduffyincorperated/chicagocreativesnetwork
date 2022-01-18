from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def index(request):
    return render(request, 'dashboard/index.html',)

def home(request):
    return render(request, 'home/index.html')

# templates we are creating
def themesIndex(request):
    return render(request, 'dashboard/themesindex.html')

def themesAbout(request):
    return render(request, 'dashboard/themesabout.html') 


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
