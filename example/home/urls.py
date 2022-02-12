from django.urls import path, include
from . import views


urlpatterns = [
    path('network', views.index, name='index'),
    # user browser
    path('themesindex', views.themesIndex, name='themesindex'),
    path('', views.themesAbout, name='themesabout'),
    path('themesnetwork', views.themesNetwork, name='themesnetwork'),
    path("home/", views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
    path("posts/<slug:_slug>/", views.post_detail, name="post_detail"),
]
