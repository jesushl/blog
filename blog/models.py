from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    def __str__(self):
        return "{self.name}  {self.level}/100".format(self=self)

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    abstract = models.CharField(max_length=128, blank=False, null=True)
    content = models.TextField(max_length=10000, blank=False, null=True)
    created = models.DateField(auto_created=True, blank=False, null=True)
    updated = models.DateField(auto_now=True, blank=False, null=True)
    ENG_LANG = 'eng'
    SPA_LANG = 'esp'
    LANGUAGE_CHOICES = [
        (ENG_LANG, 'english'),
        (SPA_LANG, 'español')
    ]
    language = models.CharField(
        max_length=3,
        choices= LANGUAGE_CHOICES,
        default=SPA_LANG
    )
    def __str__(self):
        return "{self.title} : {self.abstract}".format(self=self)

class Hobby(models.Model):
    name = models.CharField(max_length=200)
    article  = models.ManyToManyField(
        Article,  
        blank=True
    )
    def __str__(self):
        return "{self.name} : {self.article.abstract}".format(self=self)


class BookRecomendation(models.Model):
    name=models.CharField(max_length=50)
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE ,
        blank=True, 
        null=True
    )
    def __str__(self):
        return "{self.name}:  {self.article.abstract}".format(self=self)

class MovieRecomendation(models.Model):
    name=models.CharField(max_length=50)
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE ,
        blank=True, 
        null=True
    )
    def __str__(self):
        return "{self.name}:  {self.article.abstract}".format(self=self)

class TechArticle(models.Model):
    name=models.CharField(max_length=50)
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE ,
        blank=True, 
        null=True
    )
    technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return "{self.name}:  {self.article.abstract}".format(self=self)

class Message(models.Model):
    email  = models.EmailField()
    message = models.TextField()
    created = models.DateField(
        auto_created=True, 
        blank=False, 
        null=False
    )
    def __str__(self):
        return (
            "{self.email}  -> {self.message} \n"
            "{self.created}"
        ).format(self=self)

class Frace(models.Model):
    frace = models.CharField(max_length=200)
    def __str__(self):
        return self.frace

class ContactCard(models.Model):
    name = models.CharField( max_length= 50)
    title = models.CharField(max_length=50)
    nickname = models.CharField(max_length=9)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20,null=True, blank=True)
    adress = models.CharField(max_length=100,null=True, blank=True)
    skype=models.CharField(max_length=20,null=True, blank=True)
    twitter=models.CharField(max_length=10, null=True, blank=True)
    linkedin=models.CharField(max_length=70,null=True, blank=True)
    
    updated = models.DateField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return (
            "{self.name} : {self.title}"
        ).format(self=self)

class JobExperience(models.Model):
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    termination_date = models.DateField()
    roll_description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    # Should have a logo for company
    contact_card = models.ForeignKey(
        ContactCard,
        on_delete=models.CASCADE,
        null=True, 
        blank=True
    )
    def __str__(self):
        return (
                       " {self.company_name} : "
                        "{self.job_title} : "
                        "{self.start_date} -> "
                        "{self.termination_date} "
        ).format(self=self)
