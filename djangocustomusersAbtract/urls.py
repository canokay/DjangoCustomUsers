from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from djangocustomusersAbstract_app.views import IndexView, JustAdminView, JustEditorView, AdminOrEditorView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView, name='index'),
    url(r'^just-admin/$', JustAdminView, name='justAdmin'),
    url(r'^just-editor/$', JustEditorView, name='justEditor'),
    url(r'^adminOrEditor/$', AdminOrEditorView, name='adminOrEditor'),
    url(r'^register/$', RegisterView, name='register'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
]
