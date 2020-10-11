# django view
from django.shortcuts import render
from django.template import Context
# models
from .models import Technology, Hobby, BookRecomendation, TechArticle
from .models import Article, JobExperience, MovieRecomendation
from .models import Frace, Message, ContactCard, JobExperience, Image
# tools
from blog.contextual.random_frace import get_random_frase 

def index(request):
    context = set_context(where_im_name='is_blog')
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


