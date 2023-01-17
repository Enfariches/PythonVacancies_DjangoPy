from django.shortcuts import render
from .models import Article, Dict



def index_page(request):
    article = Article.objects.all()[0]
    context = {'article': article}
    return render(request, 'main/index.html', context)

def base(requset):
    return render(requset, 'main/base.html')

def demand_page(requset):
    salary_by_years = Dict.objects.all()[0]
    vacs_by_years = Dict.objects.all()[1]
    vac_salary_by_years = Dict.objects.all()[2]
    vac_counts_by_years = Dict.objects.all()[3]
    heads1 = Dict.objects.all()[6]
    context = {'salary_by_years': salary_by_years, 'vacs_by_years': vacs_by_years,
               'vac_salary_by_years': vac_salary_by_years, 'vac_counts_by_years': vac_counts_by_years,
               'heads1': heads1,}
    return render(requset, 'main/demand.html', context)

def geography_page(requset):
    heads2 = Dict.objects.all()[9]
    salary_by_cities = Dict.objects.all()[4]
    vacs_by_cities = Dict.objects.all()[5]
    context = {"heads2": heads2, "salary_by_cities": salary_by_cities, "vacs_by_cities": vacs_by_cities}
    return render(requset, 'main/geography.html', context)

def skills_page(requset):
    return render(requset, 'main/skills.html')

def lastvacancy_page(requset):
    return render(requset, 'main/lastvacancy.html')
