from django.shortcuts import render

def index_page(request):
    return render(request, 'main/index.html')

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
