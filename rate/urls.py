from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register_request,name='register'),
    path("login", views.login_request, name="login"),
    path("sub", views.submit_request, name='submit'),
    path("detail/<id>", views.project_detail,name="details"),
    path('search/',views.project_search,name='searchResults'),
    path("projects",views.project_list,name='projects'),
    path("all_users",views.all_users,name='allUsers'),
    path('ratings/<project_id>', views.project_ratings,name='ratings'),
    path('logout', views.logout_request, name='logout'),


    



]