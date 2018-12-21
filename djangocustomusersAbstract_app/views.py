from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from djangocustomusersAbtract.decorators import admin_only, role_required
from djangocustomusersAbtract.forms import LoginForm, RegisterForm


def IndexView(request):
    return render(request, 'index.html')


def RegisterView(request):
    """if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            status = form.cleaned_data.get("status")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.set_status(status)

            newUser.save()
            login(request, user)
    else:
        form = RegisterForm()
        context = {
            "form": form
        }"""
    form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "register-2.html", context)


def LoginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, "login.html", context)

        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


def LogoutView(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
@admin_only
def JustAdminView(request):
    return render(request, 'justAdmin.html')


@login_required(login_url="login")
@role_required(allowed_roles=["editor"])
def JustEditorView(request):
    return render(request, 'justEditor.html')


@login_required(login_url="login")
@role_required(allowed_roles=["admin", "editor"])
def AdminOrEditorView(request):
    return render(request, 'adminOrEditor.html')
