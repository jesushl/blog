# django view
from django.shortcuts import render
from django.template import Context
# models
from .models import Article, JobExperience, Technology
from .models import Frace, Message, ContactCard, JobExperience, Image
# tools
from blog.contextual.random_frace import get_random_frase 

def index(request):
    context = set_context(where_im_name='is_blog')
    articles = Article.objects.all().order_by('-updated')[:10]
    context.update({'articles': articles})
    tech_articles = Article.objects.filter(article_type=Article.TECH_ART).order_by('-updated')[:10]
    context.update({'tech_articles': tech_articles })
    return  render(request, 'index.html', context)

def resume(request):
    context = set_context(where_im_name='is_resume')
    _contact_card_info = ContactCard.objects.get(id=1)
    context.update({'contact': _contact_card_info})
    contact_image = Image.objects.get(id=_contact_card_info.image.id)
    context.update({'contact_image': contact_image})
    experiences = JobExperience.objects.filter(
        contact_card=_contact_card_info
        ).order_by(
            '-start_date'
        )
    context.update({'experience_items': list()})
    for experience in experiences:
        technologies = Technology.objects.filter(jobexperience=experience)
        context['experience_items'].append(
                {'experience': experience, 'technologies': technologies, 'image': experience.image }
        )
    return render(request, "curriculum.html", context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = set_context(where_im_name=article.title)
    context.update({'article': article})
    return render(request, 'article.html', context)

# Utils
def set_context(
    context=None, 
    where_im_name:bool=None
)->dict:
    _context = {}
    _context.update({where_im_name: True}) # where im boolean tag
    _context.update({'frace': get_random_frase()})
    if not context:
        context = _context
    else:
        context.update(_context)
    return context


