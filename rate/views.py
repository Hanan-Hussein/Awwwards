from multiprocessing import context
from django.shortcuts import render
from .forms import Registration, LoginForm, SubmitForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Project
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
@login_required
def home(request):
    projects=Project.objects.all()
    return render(request,'home.html',context={"projects":projects})

def register_request(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful, Please Login")
            return redirect("login")
        messages.error(
            request, "Unsuccessful registration.Please ensure you have entered a strong password and valid email")
    form = Registration()
    return render(request, template_name="auth/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'auth/login.html', context=context)


@login_required
def submit_request(request):
    if request.method == "POST":
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description =form.cleaned_data["description"]
            site_url = form.cleaned_data["site_url"]
            landing_page = form.cleaned_data["landing_page"]
            new_project = Project(title=title, description=description,site_url=site_url)
            new_project.landing_page = landing_page
            new_project.owner = request.user
            new_project.save()
            messages.success(request,"Project uploaded successfully 🎊👏🏽") 
            return redirect('home')
    
    form = SubmitForm()
    context = {
        "form": form,
    }
    return render(request, 'submit.html',context=context)


@login_required
def project_detail(request,id):
    projects=Project.objects.get(id=id)
    print(projects.title)
    return render(request, 'details.html',context={"projects":projects})

@login_required
def project_search(request):
    projects=Project.objects.all()
    if 'name' in request.GET and request.GET['name']:
        searched_term = request.GET['name']
        searched = Project.search_project(searched_term)
        message = f"{searched_term}"
     
        return render(request, 'search_results.html', {"message": message, 'searched': searched})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html', {"message": message})

@api_view(['GET','POST'])
def project_list(request):
    if request.method=='GET':
        projects=Project.objects.all()
        serializer=ProjectSerializer(projects,many=True)
        return Response(serializer.data)
        # return JsonResponse({"projects":serializer.data},safe=False)