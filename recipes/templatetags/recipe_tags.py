from django import template
from django.db.models import Count

import recipes.views as views
from recipes.models import Category, TagPost
from recipes.utils import menu

register = template.Library()


@register.simple_tag
def get_menu():
    return menu


@register.inclusion_tag('recipe/list_categories.html')
def show_categories(cats_selected=0):
    cats = Category.objects.annotate(
        total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cats_selected}


@register.inclusion_tag('recipe/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(
        total=Count('tags')).filter(total__gt=0)}
