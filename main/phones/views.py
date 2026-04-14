from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    params = request.GET.get('sort')
    phones = list(Phone.objects.all())

    if params in ['name', 'min_price', 'max_price']:

        if params == 'name':
            phones.sort(key=lambda x: x.name)

        if params == 'min_price':
            phones.sort(key=lambda x: x.price)

        if params == 'max_price':
            phones.sort(key=lambda x: -x.price)

    template = 'catalog.html'
    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    rec_phones = Phone.objects.get(slug=slug)
    context = {'phone': rec_phones}

    return render(request, template, context)