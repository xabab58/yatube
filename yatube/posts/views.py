from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def ice_cream_list(request):
    return HttpResponse('Список постов')


def ice_cream_detail(request, slug):
    return HttpResponse(f'Пост номер {slug}')