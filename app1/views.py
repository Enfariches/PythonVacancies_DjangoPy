from django.shortcuts import render
from .models import Article, Dict
import json
import requests



def index_page(request):
    article = Article.objects.get(title='main_page')
    context = {'article': article}
    return render(request, 'main/index.html', context)

def base(requset):
    return render(requset, 'main/base.html')

def form_page(requset):
    return render(requset, 'main/form.html')

def demand_page(requset):
    salary_by_years = Dict.objects.get(title='salary_by_years')
    vacs_by_years = Dict.objects.get(title='vacs_by_years')
    vac_salary_by_years = Dict.objects.get(title='vac_salary_by_years')
    vac_counts_by_years = Dict.objects.get(title='vac_counts_by_years')
    heads1 = Dict.objects.get(title='heads1')
    article = Article.objects.get(title='demand_page')
    context = {'salary_by_years': salary_by_years, 'vacs_by_years': vacs_by_years,
               'vac_salary_by_years': vac_salary_by_years, 'vac_counts_by_years': vac_counts_by_years,
               'heads1': heads1, 'article': article}
    return render(requset, 'main/demand.html', context)

def geography_page(requset):
    heads2 = Dict.objects.get(title='heads2')
    salary_by_cities = Dict.objects.get(title='salary_by_cities')
    vacs_by_cities = Dict.objects.get(title='vacs_by_cities')
    article = Article.objects.get(title='geography_page')
    context = {"heads2": heads2, "salary_by_cities": salary_by_cities, "vacs_by_cities": vacs_by_cities,
               'article': article}
    return render(requset, 'main/geography.html', context)

def skills_page(requset):
    article = Article.objects.get(title='skills_page')
    context = {'article': article}
    return render(requset, 'main/skills.html', context)

def lastvacancy_page(requset):
        url = 'https://api.hh.ru/vacancies?text=python+OR+%D0%BF%D0%B8%D1%82%D0%BE%D0%BD+OR+%D0%BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD&date_from=2022-12-31&date_to=2022-12-31'
        response = requests.get(url).text
        vacancies = sorted(json.loads(response)["items"], key=lambda vac: int(vac['published_at'][8:10]), reverse=True)[
                    :10]
        full_vac = []
        for vacancy in vacancies:
            response = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').text
            full_vac.append(json.loads(response))
        return render(requset, 'main/lastvacancy.html', {'vacancies': full_vac})
