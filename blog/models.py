from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    # Should have a logo too

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    abstract = models.CharField(max_length=128, blank=False, null=True)
    content = models.TextField(max_length=10000, blank=False, null=True)
    created = models.DateField(auto_created=True, blank=False, null=True)
    updated = models.DateField(auto_now=True, blank=False, null=True)


class Hobby(models.Model):
    name = models.CharField(max_length=200)
    article  = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )

class JobExperience(models.Model):
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    termination_date = models.DateField()
    roll_description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    # Should have a logo for company
        
class BookRecomendation(models.Model):
    name=models.CharField(max_length=50)
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE ,
        blank=True, 
        null=True
    )

class MovieRecomendation(models.Model):
    name=models.CharField(max_length=50)
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE ,
        blank=True, 
        null=True
    )

class TechArticle(models.Model):
    name=models.CharField(max_length=50)
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE ,
        blank=True, 
        null=True
    )