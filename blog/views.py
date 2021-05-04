# django view
from django.shortcuts import render, redirect
from django.template import Context
# models
from .models import Article, JobExperience, Technology
from .models import Frace, Message, ContactCard, JobExperience, Image
# tools
from blog.contextual.random_frace import get_random_frase
# Form
from blog.forms import ContactForm
# Mail
from django.core.mail import send_mail


def index(request):
    context = set_context(where_im_name='is_index')
    articles = Article.objects.all().order_by('-updated')[:10]
    context.update({'articles': articles})
    tech_articles = Article.objects.filter(
        article_type=Article.TECH_ART
    ).order_by('-updated')[:6]
    context.update({'tech_articles':  tech_articles})
    hobby_articles = Article.objects.filter(
        article_type=Article.HOBBY_ART
    ).order_by("-updated")[:6]
    context.update({'hobby_articles':  hobby_articles})
    return render(request, 'index.html', context)


def resume(request):
    context = set_context(where_im_name='is_resume')
    _contact_card_info = ContactCard.objects.get(id=1)
    context.update({'contact': _contact_card_info})
    contact_image = Image.objects.get(id=_contact_card_info.image.id)
    context.update({'contact_image': contact_image})
    experiences = JobExperience.objects.all(
        ).order_by(
            '-start_date'
        )
    context.update({'experience_items': list()})
    for experience in experiences:
        technologies = Technology.objects.filter(jobexperience=experience)
        context['experience_items'].append(
                {
                    'experience': experience, 'technologies': technologies,
                    'image':  experience.image
                }
        )
    return render(request, "curriculum.html", context)


def article(request, article_id):
    context = set_context(where_im_name='is_blog')
    article = Article.objects.get(id=article_id)
    context.update({'article': article})
    return render(request, 'article.html', context)


def blog(request, page=1):
    if page >= 1:
        context = set_context(where_im_name='is_blog')
        articles_by_page = 10
        max_articles = Article.objects.all().count()
        button_article = (page - 1) * articles_by_page
        last_article = button_article + articles_by_page
        if last_article > max_articles:
            last_article = max_articles - button_article
        if page > 1:
            context.update({'previous_page':  page - 1})
        else:
            context.update({'previous_page': False})
        # is a valid next page ?
        next_page = page + 1
        if next_page <= round(max_articles / articles_by_page):
            context.update({'next_page': next_page})
        else:
            context.update({'next_page': False})
        context.update({'current_page': page})
        articles = Article.objects.all().order_by('-updated')[
            button_article: last_article
        ]
        context.update({'articles': articles})
        return render(request, 'blog.html', context)
    return render(request, 'index.html')


def me(request):
    context = set_context(where_im_name='is_me')
    article = Article.objects.filter(
        article_type=Article.MY_PROFILE
    ).order_by('-updated')
    if article:
        article = article[0]
        context.update({'article':  article})
    return render(request, 'article.html', context)


def contact(request):
    context = set_context()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            try:
                send_mail(
                    "test",
                    'Test message',
                    'test@example.com',
                    ['j3su5.pro@gmail.com'],
                    fail_silently=False
                )

            except ConnectionRefusedError:
                pass
            return redirect('index')
        else:
            context.update({'form': form})
            return render(request, 'contact_form.html', context=context)
    else:
        form = ContactForm()
        context.update({'form': form})
        return render(request, 'contact_form.html', context=context)


# Utils
def set_context(
    context=None,
    where_im_name: bool = None
) -> dict:
    _context = {}
    _context.update({where_im_name: True})   # where im boolean tag
    _context.update({'frace': get_random_frase()})
    if not context:
        context = _context
    else:
        context.update(_context)
    return context
