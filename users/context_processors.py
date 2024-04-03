from recipes.utils import menu


def get_recipe_context(request):
    return {'main_menu': menu}
