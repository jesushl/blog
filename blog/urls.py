from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('blog/<int:page>/', views.blog, name='blog'),
    path('me', views.me, name='me'),
    path('contact', views.contact, name="contact")
] + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
