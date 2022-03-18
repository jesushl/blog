from django.shortcuts import render


def auth(request):
    import pdb; pdb.set_trace()
    return render(request, 'home.html')


def login_google():
    pass
