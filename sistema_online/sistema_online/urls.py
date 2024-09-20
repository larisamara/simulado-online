from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('questoes/', include('questoes.urls')),
    path('simulados/', include('simulados.urls')),
]

