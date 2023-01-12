from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dishes(request, name_dish):
    serving = int(request.GET.get('servings', 1))
    context = {
        'recipe': {

        }
    }
    if name_dish in DATA:
        for ingredient in DATA[name_dish]:
            context['recipe'][ingredient] = DATA[name_dish][ingredient] * serving
    return render(request, 'calculator/index.html', context)
