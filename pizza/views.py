from django.shortcuts import render


def catalog_view(request):
    if request.method == 'GET':
        return render(request, 'pizza/catalog.html', {'title': 'Catalog'})
