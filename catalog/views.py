from django.shortcuts import render


def main(request):
    context = {
        'title': "Главная"
    }
    return render(request, 'catalog/main.html', context)


def catalog(request):
    context = {
        'title': "Каталог"
    }
    return render(request, 'catalog/catalog.html', context)


def category(request):
    context = {
        'title': "Категория 1"
    }
    return render(request, 'catalog/category.html', context)


def contact(request):
    context = {
        'title': "Контакты"
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone}, {message}")

    return render(request, 'catalog/contact.html', context)
