from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from CustomUsers.views import IndexView, JustAdminView, JustEditorView, AdminOrEditorView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView, name='index'),
    url(r'^just-admin/$', JustAdminView, name='justAdmin'),
    url(r'^just-editor/$', JustEditorView, name='justEditor'),
    url(r'^adminOrEditor/$', AdminOrEditorView, name='adminOrEditor'),
]
