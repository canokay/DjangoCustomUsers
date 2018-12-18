from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from DjangoCustomUsers.decorators import admin_only, role_required


def IndexView(request):
    return render(request, 'index.html')


@login_required(login_url="index")
@admin_only
def JustAdminView(request):
    return render(request, 'justAdmin.html')


@login_required(login_url="index")
@role_required(allowed_roles=[2])
def JustEditorView(request):
    return render(request, 'justEditor.html')


@login_required(login_url="index")
@role_required(allowed_roles=[1, 2])
def AdminOrEditorView(request):
    return render(request, 'adminOrEditor.html')
