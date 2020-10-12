from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('blog/<int:page>/',views.blog, name='blog' )
]