"""
URL configuration for flight project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView

from flight import views
from flight.views import get_flight

urlpatterns = [
    path('', views.intro_view, name='intro'),
    path('main.html', views.main_view, name='main'),
    path('get_flight/', get_flight, name='get_flight'),
    path('static/graphics/airports.png', RedirectView.as_view(url=settings.STATIC_URL +
                                                                  'graphics/airports.png', permanent=True)),
    path('game.html', views.game_view, name='game')

]

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
