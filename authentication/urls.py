from . import views
from django.urls import path

urlpatterns = [
    path("", views.auth, name="auth"),
    path("callback", views.login_google, name="google"),
    
]
