from . import views
from django.urls import path

urlpatterns = [
    path("auth", views.auth, name="auth"),
    path("google", views.login_google, name="google"),
]
