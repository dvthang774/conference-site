from django.shortcuts import render


def home(request):
    context = {}
    template = 'pages/home.html'
    return render(request, template, context)
