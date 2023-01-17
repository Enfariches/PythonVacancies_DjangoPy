from django.contrib import admin
from .models import Article, Dict

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Dict)
class DictAdmin(admin.ModelAdmin):
    pass