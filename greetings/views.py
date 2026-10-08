from django.shortcuts import render

from .forms import UserNameForm


def home(request):

    greeting = ""


    if request.method == "POST":

        form = UserNameForm(request.POST)


        if form.is_valid():

            user = form.save()

            greeting = (
                f"Здравствуйте, {user.name}!"
            )

    else:

        form = UserNameForm()


    return render(
        request,
        "home.html",
        {
            "form": form,
            "greeting": greeting
        }
    )
