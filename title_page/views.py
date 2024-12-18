from django.shortcuts import render, redirect

from title_page.models import Item


def index(request):
    """Home page"""
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
