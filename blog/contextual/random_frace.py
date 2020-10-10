# python
import random as ra
# Models
from blog.models import Frace

def get_random_frase():
    number_of_many_frases = Frace.objects.all().count()
    frace_index = ra.randrange(0, number_of_many_frases)
    return Frace.objects.all()[frace_index].frace