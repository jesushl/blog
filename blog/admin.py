from django.contrib import admin

# Register your models here.
from .models import Article, JobExperience
from .models import Frace, Message, ContactCard, Image
from .models import Technology

admin.site.register(Article)
admin.site.register(JobExperience)
admin.site.register(Frace)
admin.site.register(Message)
admin.site.register(ContactCard)
admin.site.register(Image)
admin.site.register(Technology)