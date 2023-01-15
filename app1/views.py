from django.shortcuts import render
from .models import Article



def index_page(request):
    article = Article.objects.all()[0]
    context = {'article': article}
    return render(request, 'main/index.html', context)

def base(requset):
    return render(requset, 'main/base.html')

def demand_page(requset):
    return render(requset, 'main/demand.html')

def geography_page(requset):
    return render(requset, 'main/geography.html')

def skills_page(requset):
    return render(requset, 'main/skills.html')

def lastvacancy_page(requset):
    return render(requset, 'main/lastvacancy.html')
