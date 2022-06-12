from django.shortcuts import render
from .forms import Registration
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

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
