from django.urls import path, include
from django.views.generic import TemplateView
# REF: https://www.section.io/engineering-education/django-google-oauth/
from . import views
urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path("profile/", views.profile, name='user_profile'),
]
