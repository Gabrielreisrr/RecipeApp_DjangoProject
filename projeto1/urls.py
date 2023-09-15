"""
URL configuration for projeto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# O arquivo URL tem como objetivo guardar todas as rotas do site, seja homepage, login, pagina principal etc.

# A função path recebe como primeiro argumento a rota que que sera requirida (request) e como segundo
# argumento a função que o servidor utilizara para mandar a resposta(response).

# Utilizando a função include do django é possivel criar um arquivo url dentro de um app 
# e herdar as rotas que foram destinada aquele app, o que facilita na oeganização.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
