from django.contrib import admin

# Register your models here.
from .models import Technology, Hobby, BookRecomendation, TechArticle
from .models import Article, JobExperience, MovieRecomendation

admin.site.register(Technology)
admin.site.register(Hobby)
admin.site.register(BookRecomendation)
admin.site.register(TechArticle)
admin.site.register(Article)
admin.site.register(JobExperience)
admin.site.register(MovieRecomendation)
