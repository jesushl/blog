from django.db import models
# ckeditor
from ckeditor_uploader.fields import RichTextUploadingField


class Technology(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return "{self.name}  {self.level}/100".format(self=self)


class Image(models.Model):
    image = models.ImageField(
        upload_to='gallery',
        default='gallery/static/images/no-img.jpg'
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    abstract = models.CharField(max_length=128, blank=False, null=True)
    content = RichTextUploadingField(max_length=10000, blank=False, null=True)
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
        choices=LANGUAGE_CHOICES,
        default=SPA_LANG
    )
    main_image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    TECH_ART = 't'
    HOBBY_ART = 'h'
    BOOK_ART = 'b'
    MOVIE_ART = 'm'
    MY_PROFILE = 'p'
    ARTICLE_TYPE_CHOICES = [
        (TECH_ART, 'Technology'),
        (HOBBY_ART, 'Hobby'),
        (BOOK_ART, 'Book'),
        (MOVIE_ART, 'Movie'),
        (MY_PROFILE, 'Profile')
    ]
    article_type = models.CharField(
        max_length=1,
        choices=ARTICLE_TYPE_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{self.title} : {self.abstract}".format(self=self)


class Message(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    email = models.EmailField()
    message = models.TextField()
    created = models.DateField(
        auto_now_add=True,
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
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    nickname = models.CharField(max_length=9)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    adress = models.CharField(max_length=100, null=True, blank=True)
    skype = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=70, null=True, blank=True)
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    updated = models.DateField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return (
            "{self.name} : {self.title}"
        ).format(self=self)


class JobExperience(models.Model):
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    termination_date = models.DateField(blank=True, null=True)
    roll_description = models.TextField()
    technologies = models.ManyToManyField(Technology)

    image = models.ForeignKey(
        Image,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (
                    " {self.company_name} : "
                    "{self.job_title} : "
                    "{self.start_date} -> "
                    "{self.termination_date} "
        ).format(self=self)
