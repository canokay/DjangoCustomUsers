from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from DjangoCustomUsers.decorators import admin_only, role_required

from CustomUsers.forms import LoginForm, UserStatusForm


def IndexView(request):
    return render(request, 'index.html')


def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


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
@role_required(allowed_roles=[2])
def JustEditorView(request):
    return render(request, 'justEditor.html')


@login_required(login_url="login")
@role_required(allowed_roles=[1, 2])
def AdminOrEditorView(request):
    return render(request, 'adminOrEditor.html')
