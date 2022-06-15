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




]