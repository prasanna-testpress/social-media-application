from django.shortcuts import render
from .forms import LoginForm

from django.contrib.auth import authenticate, login


def login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data

            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                login(request, user)
                return render(request, "account/dashboard", {"section": "dashboard"})
            else:

                return render(
                    request,
                    "account/login.html",
                    {"form": form, "error": "Invalid Credentials"},
                )

    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})
