from django.shortcuts import render,redirect
from .forms import LoginForm

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



def user_login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data

            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                login(request, user)
                return redirect("account:dashboard")
            else:

                return render(
                    request,
                    "account/login.html",
                    {"form": form, "error": "Invalid Credentials"},
                )

    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return render(request, 'account/logout.html')


@login_required
def dashboard(request):

    return render(request, "account/dashboard.html", {"section": "dashboard"})
