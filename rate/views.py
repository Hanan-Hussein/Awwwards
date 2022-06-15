
from django.shortcuts import render
from .forms import Registration, LoginForm, SubmitForm, ProfileEditForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Ratings
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required
def home(request):
    projects=Project.objects.all()
    user_display = request.user

    return render(request,'home.html',context={"projects":projects,"user_display":user_display})

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
    user_display = request.user

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
        "user_display":user_display
    }
    return render(request, 'submit.html',context=context)


@login_required
def project_detail(request,id):
    projects=Project.objects.get(id=id)
    user_display = request.user

    reviews = Ratings.objects.filter(project=projects)
    print(projects.title)
    return render(request, 'details.html',context={"projects":projects,'ratings':reviews,'user_display':user_display} )

@login_required
def project_search(request):
    projects=Project.objects.all()
    if 'name' in request.GET and request.GET['name']:
        searched_term = request.GET['name']
        user_display = request.user

        searched = Project.search_project(searched_term)
        message = f"{searched_term}"
     
        return render(request, 'search_results.html', {"message": message, 'searched': searched, 'user_display':user_display})
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

@api_view(['GET','POST'])
def all_users(request):
    if request.method =='GET':
        users=User.objects.all()
        serializer=ProfileSerializer(users, many=True)
        return Response(serializer.data)
        

@csrf_exempt
def project_ratings(request, project_id):
    current_user = request.user
    project=Project.objects.all().get(id=project_id)
    # Returns a tuple the object is in the first position
    rating = Ratings.objects.get_or_create(
        user=current_user, project=project)[0]
    type = request.POST.get('type')
    value = request.POST.get('value')
    if type == 'usability':
        rating.usability = value
        rating.save()
    elif type == 'content':
        rating.content = value
        rating.save()
    elif type == 'design':
        rating.design = value
        rating.save()
    print(rating)
    print(Ratings.objects.all().filter(project__id=project_id))
    return HttpResponse()

def logout_request(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user_display=request.user
    current_user = request.user
    posts=Project.objects.filter(owner=current_user)
    context = {
    "user_details": current_user,
    "user_display": user_display,
    "posts": posts,
    'number': len(Project.objects.all().filter(owner=request.user.id)),


    }
    return render(request,'profile.html', context=context)


@login_required
def profile_edit(request):
    user_display = request.user

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            profilephoto = form.cleaned_data['profilephoto']
            profile = Profile.objects.get(id=request.user.id)
            profile.profilephoto = profilephoto
            profile.bio = bio
            profile.save()
            User.objects.filter(id=request.user.id).update(
                email=email, username=username)
            return redirect('profile')
    current_user = request.user
    user_profile = Profile.objects.all().filter(
        user=current_user).first()
    form = ProfileEditForm()
    context = {
        "user_details": user_display,
        "form": form,
        "user_display": user_display,
        'number': len(Project.objects.all().filter(owner=request.user.id)),
       
    }
    return render(request, 'profile_edit.html', context=context)
