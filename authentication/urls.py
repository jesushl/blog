from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
# REF: https://www.section.io/engineering-education/django-google-oauth/

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path("accounts/",include("allauth.urls")),
    path("logout/",LogoutView.as_view()),

]
